#!/usr/bin/env python
"""索引重建：从条目 frontmatter 生成两级索引。
用法：python rebuild_index.py
产出：
  1. references/_index/<分类>.md          —— 分类索引（瘦身：去 signals 列）
  2. references/_index/_by-age/<年龄段>.md —— 年龄段横向索引（拿月龄直接读，跨分类）
蒸馏代理只写条目；索引一律由主会话跑本脚本生成（并行安全）。"""
import os, re, glob, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# scripts/ → baby-distill/ → skills/ → baby-tutor/
REFS = os.path.join(ROOT, 'references')
IDX = os.path.join(REFS, '_index')
AGE = {
 'newborn-early':'0-7天','newborn-adaptation':'8-28天','infant-1-2-months':'1-2月',
 'infant-2-3-months':'2-3月','infant-3-4-months':'3-4月','infant-4-6-months':'4-6月',
 'infant-6-9-months':'6-9月','infant-9-12-months':'9-12月','toddler-12-15-months':'12-15月',
 'toddler-15-18-months':'15-18月','toddler-18-24-months':'18-24月','child-2-3-years':'2-3岁',
 'child-3-4-years':'3-4岁','child-4-5-years':'4-5岁','child-5-6-years':'5-6岁'}
# 年龄段横向索引的分段（每条目出现在它覆盖的所有段）
BANDS = [
 ('0-6月', ['newborn-early','newborn-adaptation','infant-1-2-months','infant-2-3-months','infant-3-4-months','infant-4-6-months']),
 ('6-12月', ['infant-6-9-months','infant-9-12-months']),
 ('1-2岁', ['toddler-12-15-months','toddler-15-18-months','toddler-18-24-months']),
 ('2-3岁', ['child-2-3-years']),
 ('3-6岁', ['child-3-4-years','child-4-5-years','child-5-6-years']),
]
ALL_AGES = set(AGE)
AGE_ORDER = list(AGE)  # 键序即月龄先后

def fmt_ages(ids):
    """紧凑月龄：全 15 段→'全(0-6岁)'；否则按时间顺序取首~尾区间。"""
    ids = [a for a in ids if a in AGE]
    if not ids: return '全(0-6岁)'
    if len(set(ids)) == len(AGE_ORDER): return '全(0-6岁)'
    ids.sort(key=AGE_ORDER.index)
    return AGE[ids[0]] if len(ids) == 1 else f'{AGE[ids[0]]}↔{AGE[ids[-1]]}'

def parse_fm(text):
    m = re.match(r'^---\n(.*?)\n---', text, re.S)
    if not m: return {}
    fm_raw = m.group(1)
    fm = {}
    for k in ['id','title','category','evidence','problem']:
        mm = re.search(rf'^{k}:\s*(.*)$', fm_raw, re.M)
        fm[k] = mm.group(1).strip() if mm else ''
    am = re.search(r'^age_range:\s*\[(.*?)\]', fm_raw, re.S | re.M)
    fm['_ages'] = [a.strip() for a in am.group(1).split(',')] if am else []
    ai = re.search(r'^also_in:\s*\[(.*?)\]', fm_raw, re.S | re.M)
    fm['_also'] = [a.strip() for a in ai.group(1).split(',')] if ai else []
    return fm

def build():
    cats = collections.defaultdict(list)
    for p in sorted(glob.glob(os.path.join(REFS, '**', '*.md'), recursive=True)):
        if '_index' in p or os.sep + '_' in p: continue
        d = os.path.dirname(p)
        cat = os.path.basename(d)
        if not re.match(r'^\d\d-', cat): continue
        fm = parse_fm(open(p, encoding='utf-8').read())
        if not fm.get('id'): continue
        fm['_cat'] = cat
        cats[cat].append(fm)
    total = 0
    # 1) 分类索引（瘦身：id|tier|月龄|判断|用户会怎么问）
    for cat, rows in sorted(cats.items()):
        disp = cat.split('-', 1)[1]
        lines = [f'# 索引 · {cat}（{len(rows)} 条）', '',
                 f'> 路径前缀 `references/{cat}/`', '',
                 '> **匹配**：先比「用户会怎么问」（逐字重合=强命中），再比「判断」（同一问题）。「月龄」列不符的先降级。',
                 '> **红旗检查**：本类所有条目回复前先扫 `red_flags`——命中先走「先说安全」。', '',
                 '| id | tier | 月龄 | 判断 | 用户会怎么问 |', '|---|---|---|---|---|']
        for fm in rows:
            ages = fmt_ages(fm['_ages'])
            lines.append(f"| `{fm['id']}` | {fm['evidence']} | {ages} | {fm['title'][:30]} | {fm['problem'][:44]} |")
            total += 1
        for oc, orows in cats.items():
            if oc == cat: continue
            for fm in orows:
                if disp in fm['_also']:
                    ages = fmt_ages(fm['_ages'])
                    lines.append(f"| `{fm['id']}` ⤴副 | {fm['evidence']} | {ages} | {fm['title'][:30]} | （主分类 {oc}，全文去主分类目录 Read） |")
        open(os.path.join(IDX, cat + '.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    # 2) 年龄段横向索引：实测反直觉——0-6月段聚合了 940+ 条（跨分类），比单一分类索引还大 9 倍，
    #    因为多数条目跨多个月龄段。故**不作为每查询读取层**，仅在 --by-age 时生成作参考。
    if '--by-age' in sys.argv:
        age_dir = os.path.join(IDX, '_by-age')
        os.makedirs(age_dir, exist_ok=True)
        for band, band_ids in BANDS:
            rows = []
            for cat, crows in cats.items():
                disp = cat.split('-', 1)[1]
                for fm in crows:
                    ages = set(fm['_ages'])
                    if (ages & set(band_ids)) or (not ages) or ages == ALL_AGES:
                        rows.append((disp, fm))
            rows.sort(key=lambda x: x[0])
            lines = [f'# 年龄段参考索引 · {band}（{len(rows)} 条）', '',
                     '> ⚠️ 仅供参考、非首选读取层——聚合了跨分类条目，体量大。检索仍以分类索引为主。', '',
                     '| 分类 | id | tier | 判断 |', '|---|---|---|---|']
            for disp, fm in rows:
                lines.append(f"| {disp} | `{fm['id']}` | {fm['evidence']} | {fm['title']} |")
            open(os.path.join(age_dir, band + '.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    print(f'重建完成: {total} 条条目, {len(cats)} 个分类索引' + (' + 年龄段参考索引' if '--by-age' in sys.argv else ''))

if __name__ == '__main__':
    build()
