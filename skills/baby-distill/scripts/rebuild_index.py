#!/usr/bin/env python
"""索引重建脚本：从条目 frontmatter 统一重建 _index/*.md。
用法：python rebuild_index.py  [--check 只校验不写]
蒸馏代理只写条目文件；索引行一律由主会话跑本脚本生成，避免并行覆盖。"""
import os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# scripts/ → baby-distill/ → skills/ → baby-tutor/
REFS = os.path.join(ROOT, 'references')
IDX = os.path.join(REFS, '_index')

# BabyForge 15 段月龄 id → 人话区间
AGE = {
 'newborn-early':'0-7天','newborn-adaptation':'8-28天','infant-1-2-months':'1-2月',
 'infant-2-3-months':'2-3月','infant-3-4-months':'3-4月','infant-4-6-months':'4-6月',
 'infant-6-9-months':'6-9月','infant-9-12-months':'9-12月','toddler-12-15-months':'12-15月',
 'toddler-15-18-months':'15-18月','toddler-18-24-months':'18-24月','child-2-3-years':'2-3岁',
 'child-3-4-years':'3-4岁','child-4-5-years':'4-5岁','child-5-6-years':'5-6岁'}

def parse_fm(text):
    m = re.match(r'^---\n(.*?)\n---', text, re.S)
    if not m: return {}
    fm = {}
    for line in m.group(1).split('\n'):
        mm = re.match(r'^(\w+):\s*(.*)$', line)
        if mm: fm[mm.group(1)] = mm.group(2).strip()
    # age_range 数组
    am = re.search(r'^age_range:\s*\[(.*?)\]', m.group(1), re.S | re.M)
    fm['_ages'] = [a.strip() for a in am.group(1).split(',')] if am else []
    # also_in 数组
    ai = re.search(r'^also_in:\s*\[(.*?)\]', m.group(1), re.S | re.M)
    fm['_also'] = [a.strip() for a in ai.group(1).split(',')] if ai else []
    return fm

def age_short(ages):
    if not ages: return '全年龄'
    return '、'.join(AGE.get(a, a) for a in ages)

def sig_short(sig_line):
    # signals 是 frontmatter 里的列表，主字段解析拿不到——从原始文本抓
    return None

def build():
    cats = {}          # cat -> [(id, tier, ages, title, problem, signals_str, also)]
    problems = {}
    signals_map = {}
    for f in sorted(glob.glob(os.path.join(REFS, '**', '*.md'), recursive=True)):
        if '_index' in f or os.sep + '_' in f: continue
        text = open(f, encoding='utf-8').read()
        fm = parse_fm(text)
        if 'id' not in fm: continue
        d = os.path.dirname(f)
        if not re.match(r'^\d\d-', os.path.basename(d)): continue
        # 抓 signals 列表（前 4 条合并）
        sm = re.search(r'^signals:\n((?:  - .*\n?)+)', text, re.M)
        sigs = [re.sub(r'^  - ', '', l).strip() for l in sm.group(1).split('\n') if l.strip()] if sm else []
        sig_str = ' / '.join(s[:28] for s in sigs[:4])
        cat = os.path.basename(os.path.dirname(f))
        cats.setdefault(cat, []).append((fm['id'], fm.get('evidence',''), age_short(fm['_ages']),
                                         fm.get('title',''), fm.get('problem',''), sig_str, fm['_also']))
    total = 0
    for cat, rows in sorted(cats.items()):
        cat_disp = cat.split('-',1)[1]
        also_rows = []  # 副分类挂靠行
        # 先按主分类输出
        lines = [f'# 索引 · {cat}（{len(rows)} 条）', '',
                 '> 路径前缀 `references/{cat}/`', '',
                 '> **匹配**：先比「用户会怎么问」（逐字重合=强命中），再比「判断」（同一问题）。`signals` 是辅助（≥2 条才算）。「月龄」列不符的先降级处理。',
                 '> **红旗检查**：本类所有条目回复前先扫 `red_flags` 字段——命中先走「先说安全」。', '',
                 '| id | tier | 月龄 | 判断 | 用户会怎么问 | signals |',
                 '|---|---|---|---|---|---|']
        for (i, tier, ages, title, problem, sig, also) in rows:
            lines.append(f'| `{i}` | {tier} | {ages} | {title} | {problem} | {sig} |')
            total += 1
        # 挂靠行（其他分类条目的 also_in 含本类）
        for other_cat, orows in cats.items():
            if other_cat == cat: continue
            for (i, tier, ages, title, problem, sig, also) in orows:
                if cat_disp in also:
                    lines.append(f'| `{i}` ⤴副 | {tier} | {ages} | {title} | {problem} | （主分类 {other_cat}，全文去主分类目录 Read） |')
        p = os.path.join(IDX, cat + '.md')
        if '--check' in sys.argv:
            if os.path.exists(p):
                cur = open(p, encoding='utf-8').read()
                if cur != '\n'.join(lines) + '\n':
                    print(f'需更新: {p} ({len(rows)} 条主分类)')
            else:
                print(f'缺失: {p}')
        else:
            open(p, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    print(f'{ "校验" if "--check" in sys.argv else "重建" }完成: {total} 条条目, {len(cats)} 个分类索引')

if __name__ == '__main__':
    build()
