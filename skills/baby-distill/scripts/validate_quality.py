#!/usr/bin/env python
"""内容质量门禁：结构之外的质量维度，批次蒸馏后必跑（与 validate_entries.py 互补）。

validate_entries.py 管"结构硬伤"（frontmatter/H1/CRLF/字段/13节/月龄id/conflicts/索引覆盖）。
本脚本管"内容质量"（这次审计真实暴露的缺陷），退出码非 0 = 不过门禁：

【硬失败 HARD】
1. 策略节残留来源/元语言：（tier-X）/（pXX）/（原书…）/ 原书/本书/书中/书里 / 蒸馏者注
   —— 正文只讲内容，出处一律只进 frontmatter.extraction 与「## 来源」节（format.md §七.12）
2. 整段重复：同一 ≥40 字段落在一个条目内出现 ≥2 次（蒸馏复制粘贴失误）
3. 中文正文半角逗号占比过高（>50% 且 >30 个）：混用标点，影响阅读
4. 空节 / 过短策略节：实操方法、核心判断等为空或 <40 字

【警告 WARN（不阻断，报告）】
5. title > 100 字（判断式标题应短）
6. 条目落在「其他·综合」兜底簇（路由不会主动选它，靠兜底才可达）——越少越好
7. 正文出现未加注的英制单位（oz / fl oz / ℉ / inch）

用法：python skills/baby-distill/scripts/validate_quality.py [--all | 一批文件路径...]
"""
import os, re, glob, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
REFS = os.path.join(ROOT, 'references')

STRATEGY_SECTIONS = ['解决的问题','核心判断','机制','诊断信号','正常范围与个体差异','实操方法',
                     '备选计策','决策规则','反模式','边界']
SRC_MARKERS = [
 (re.compile(r'[（(]\s*tier[-\s]?[1-4][^）)]*[）)]'), '（tier-X）括注'),
 (re.compile(r'[（(]\s*p{1,2}\s*\.?\s*\d'), '（pXX）页码'),
 (re.compile(r'[（(]\s*(?:原书|本书|书内|原文|书中)[^）)]*[）)]'), '（原书/本书…）括注'),
]
# 软警告：叙述口气（"原书说…""书里指出…"）。属内部菜单行文、不直接面向家长
# （答案骨架会去掉），全库普遍，不阻断门禁；有意清理时按批改写。
SOFT_MARKERS = [
 (re.compile(r'蒸馏者注'), '蒸馏者注（标记非本书内容，可接受，建议改“补充说明”措辞）'),
 (re.compile(r'原书|本书|书中|书里'), '正文叙述口气“原书/本书/书中/书里”（可改为直接陈述）'),
]
PUNCT_BAD = re.compile(r'[，。；：！？]')

def sections_of(body):
    out = collections.OrderedDict()
    parts = re.split(r'\n## ', body)
    for i, p in enumerate(parts):
        lines = p.split('\n')
        name = lines[0].strip().lstrip('# ').strip()
        # 归一：去掉标题里 "（按优先级）""(附)" 等后缀，按主体名归档
        mm = re.match(r'[^（(]+', name)
        name = (mm.group(0).strip() if mm else name) or name
        out[name] = '\n'.join(lines[1:])
    return out

def check(path):
    hard, warn = [], []
    raw = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---\n', raw, re.S)
    if not m: return hard, warn
    fm, body = m.group(1), raw[m.end():]
    secs = sections_of(body)
    # 1. 策略节来源/元语言
    for s in STRATEGY_SECTIONS:
        txt = secs.get(s, '')
        for rx, label in SRC_MARKERS:
            if rx.search(txt):
                hard.append(f'策略节「{s}」残留{label}')
                break
        for rx, label in SOFT_MARKERS:
            if rx.search(txt):
                warn.append(f'策略节「{s}」有{label}')
                break
    # 2. 整段重复
    paras = [x.strip() for x in body.split('\n') if len(re.sub(r'\s','',x)) >= 40]
    k = collections.Counter(re.sub(r'\s','',x) for x in paras)
    dups = [c for c, n in k.items() if n > 1]
    if dups: hard.append(f'整段重复 {len(dups)} 处')
    # 3. 半角逗号
    cjk = sum(1 for ch in body if '一' <= ch <= '鿿')
    half, full = body.count(','), body.count('，')
    if cjk > 300 and half > 30 and half > full: hard.append(f'半角逗号过多({half} 个, 全角{full})')
    # 4. 空/过短策略节
    for s in ['核心判断','机制','实操方法','决策规则']:
        if len(secs.get(s, '').strip()) < 40: hard.append(f'「{s}」过短或为空')
    # 5. title
    tm = re.search(r'^title:\s*(.*)$', fm, re.M)
    if tm and len(tm.group(1)) > 100: warn.append(f'title 过长({len(tm.group(1))}字)')
    # 7. 英制单位
    if re.search(r'\d+\s*(?:oz|fl oz|inches?|℉)', body): warn.append('含未换算的英制单位(oz/℉/inch)')
    return hard, warn

def cluster_index():
    """id -> 簇名，用于判断是否落在兜底簇。"""
    idx = {}
    for f in glob.glob(os.path.join(REFS, '_index', 'clusters', '*', '*.md')):
        nm = os.path.basename(f)
        if nm == '_副.md': continue
        for line in open(f, encoding='utf-8'):
            mm = re.match(r'^\|\s*`([^`]+)`', line)
            if mm: idx[mm.group(1).replace(' ⤴副','').strip()] = nm
    return idx

def main():
    args = sys.argv[1:]
    if args and args[0] != '--all':
        files = [p for p in args if p.endswith('.md')]
    else:
        files = [p for p in glob.glob(os.path.join(REFS, '**', '*.md'), recursive=True)
                 if '_index' not in p and re.match(r'^\d\d-', os.path.basename(os.path.dirname(p)))]
    cidx = cluster_index()
    hard = collections.defaultdict(list); warn = collections.defaultdict(list)
    for p in files:
        h, w = check(p)
        idm = re.search(r'^id:\s*(\S+)', open(p, encoding='utf-8').read(), re.M)
        eid = idm.group(1) if idm else os.path.basename(p)
        for x in h: hard[x.split('(')[0][:24]].append(eid)
        for x in w: warn[x.split('(')[0][:24]].append(eid)
        if eid in cidx and '其他' in cidx[eid]: warn['落在兜底簇'].append(eid)
    print(f'内容质量门禁: 检查 {len(files)} 条')
    if not hard:
        print('  ✅ 硬门禁通过')
    else:
        for k, v in sorted(hard.items(), key=lambda x: -len(x[1])):
            print(f'  ❌ {k}: {len(v)} → {v[:4]}')
    for k, v in sorted(warn.items(), key=lambda x: -len(x[1])):
        print(f'  ⚠️  {k}: {len(v)} → {v[:4]}')
    sys.exit(1 if hard else 0)

if __name__ == '__main__':
    main()
