#!/usr/bin/env python
"""格式机械验收：蒸馏每批完成后运行，一次性查出结构性硬伤。
用法：python validate_entries.py
检查项（本批蒸馏曾真实踩坑，固化为强制检查）：
  1. frontmatter 有闭合 ---（曾多次缺失）
  2. 正文有 H1 标题（曾缺 18+6 条）
  3. 无 CRLF / BOM（曾混入 7 条）
  4. 15 个必填字段齐全
  5. 正文 13 节齐全
  6. age_range 的 id 全部合法
  7. conflicts_with 引用的 id 存在
  8. id 全库唯一
  9. 每条都进了索引"""
import os, re, glob, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
REFS = os.path.join(ROOT, 'references')
AGE_IDS = {'newborn-early','newborn-adaptation','infant-1-2-months','infant-2-3-months',
 'infant-3-4-months','infant-4-6-months','infant-6-9-months','infant-9-12-months',
 'toddler-12-15-months','toddler-15-18-months','toddler-18-24-months','child-2-3-years',
 'child-3-4-years','child-4-5-years','child-5-6-years'}
REQUIRED = ['id','title','category','age_range','evidence','red_flags','extraction',
            'problem','problem_variants','signals','tradeoffs','sources']
SECTIONS = ['解决的问题','核心判断','机制','诊断信号','正常范围与个体差异','实操方法',
            '备选计策','决策规则','反模式','边界','就医红线','代价与风险提示','来源']

def main():
    errors = collections.defaultdict(list)
    ids = {}
    entries = [p for p in glob.glob(os.path.join(REFS,'**','*.md'), recursive=True) if '_index' not in p]
    for p in entries:
        name = os.path.basename(p)
        raw = open(p,'rb').read()
        if raw[:3] == b'\xef\xbb\xbf': errors['BOM'].append(name)
        if b'\r\n' in raw: errors['CRLF'].append(name)
        t = raw.decode('utf-8-sig').replace('\r\n','\n')
        m = re.match(r'^---\n(.*?)\n---\n', t, re.S)
        if not m: errors['frontmatter未闭合'].append(name); continue
        fm = m.group(1)
        if not re.search(r'^# ', t[m.end():], re.M): errors['缺H1'].append(name)
        for k in REQUIRED:
            if not re.search(rf'^{k}:', fm, re.M): errors['缺字段:'+k].append(name)
        idm = re.search(r'^id:\s*(\S+)', fm, re.M)
        if idm:
            if idm.group(1) in ids: errors['id重复'].append(f'{name} vs {ids[idm.group(1)]}')
            ids[idm.group(1)] = name
        am = re.search(r'^age_range:\s*\[(.*?)\]', fm, re.S|re.M)
        if am:
            for a in [x.strip() for x in am.group(1).split(',') if x.strip()]:
                if a not in AGE_IDS: errors['非法月龄id'].append(f'{name}:{a}')
        # 13 节
        body = t[m.end():]
        for s in SECTIONS:
            if f'## {s}' not in body: errors['缺节:'+s].append(name)
    # conflicts_with 悬空
    for p in entries:
        fm = re.match(r'^---\n(.*?)\n---', open(p,encoding='utf-8').read(), re.S)
        if not fm: continue
        cm = re.search(r'^conflicts_with:\s*\[(.*?)\]', fm.group(1), re.S|re.M)
        if cm:
            for cid in re.findall(r'[\w-]+', cm.group(1)):
                if cid and cid not in ids:
                    errors['conflicts悬空'].append(f'{os.path.basename(p)}→{cid}')
    # 索引覆盖
    indexed = set()
    for f in glob.glob(os.path.join(REFS,'_index','*.md')):
        for line in open(f,encoding='utf-8'):
            mm = re.match(r'^\|\s*`([^`]+)`', line)
            if mm: indexed.add(mm.group(1).replace(' ⤴副','').strip())
    for i in ids:
        if i not in indexed: errors['未入索引'].append(i)

    print(f'检查 {len(entries)} 条条目:')
    if not errors:
        print('  ✅ 全部通过')
    else:
        for k, v in sorted(errors.items()):
            print(f'  ❌ {k}: {len(v)} → {v[:5]}')
        sys.exit(1)

if __name__ == '__main__':
    main()
