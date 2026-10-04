# baby-tutor · 0-6 岁科学育儿知识库与 Skill

把 0-6 岁育儿问题，变成**安全优先、月龄路由、原文蒸馏**的方法论解答。

家长带着一个育儿困扰来（"宝宝半夜老醒""两岁打人怎么办""要不要做睡眠训练"），它先做安全筛查，再按孩子月龄路由到知识库，给出一份**能落地的策略**——不是泛泛建议，也不是网上传言。

## 具备的能力

| 能力 | 说明 |
|---|---|
| **安全门（最高优先级）** | 命中红旗症状（3 月内发热、呼吸窘迫、脱水、抽搐、坠落伴意识改变等）→ 只输出就医指导，跳过一切方法论。育儿错误建议有身体代价，安全压过一切 |
| **月龄路由** | 方法高度依赖月龄（8 个月的夜醒和 3 岁的夜醒是两个问题），未说月龄时必问 |
| **两级索引 + LLM 路由** | 读全库簇表（`_route.md`）按理解判断「分类 · 簇」→ 读该簇子索引双通道匹配条目。不做向量库 / 服务 / MCP |
| **策略优先输出** | 清晰的观点 + 可执行的步骤 + 2-3 条备选（含适用家庭、代价、就医红线）；来源与证据压成末尾一行 |
| **争议消解** | 对立流派（睡眠训练 vs 亲密育儿、BLW vs 勺喂…）给默认推荐 + 说清各派适用家庭，不假装只有一种答案、更不自相矛盾 |
| **证据分级** | 每条标 tier-1 机构指南 / tier-2 同行评议 / tier-3 专家专著 / tier-4 流行理念 |

## 知识库

- **1731 条方法论条目，10 分类**，全部来自 **69 本书的原文实文蒸馏**（`extraction` 字段可溯源到书名 + 章节/页码 / 官方 URL）；非原书、盗版、读书笔记、OCR 乱码一律不收录
- 每条 **15 字段 frontmatter + 13 节正文**（含育儿特有的「正常范围与个体差异」「就医红线」两节）
- 跨书对立流派双边标 `conflicts_with`，消费端据此消解矛盾

| 分类 | 条数 | 主要来源 |
|---|---|---|
| 00-安全与就医红旗 | 282 | AAP 育儿百科、崔玉涛、裴洪岗、虾米妈咪、冀连梅、Science of Mom、官方指南 |
| 01-睡眠 | 186 | Precious Little Sleep、法伯、Weissbluth、Kast-Zahn、实用程序育儿法、小土大橙子、Mindell、Karp |
| 02-喂养与营养 | 233 | Satter、崔玉涛、Science of Mom、Eliot、BLW |
| 03-情绪与安抚 | 72 | Karp 5S、Hogg、RIE、Lieberman |
| 04-管教与边界 | 211 | 蒙氏、Siegel、Faber、Greene、Phelan、德雷克斯、Gordon、Karp |
| 05-发展与里程碑 | 262 | AAP、Eliot、崔玉涛、Lieberman、Wonder Weeks |
| 06-游戏与早教 | 205 | 蒙氏（3 本）、Dirksen、RIE、Eliot、Cohen、Hanscom、NurtureShock、Suskind |
| 07-生活自理与习惯 | 127 | AAP、Jana、蒙氏、Azrin-Foxx、Glowacki、Payne |
| 08-社交与分离 | 67 | Gonzalez-Mina、Fraiberg |
| 09-父母自身 | 86 | Mindell、佩里、雷诺、Oster、高普尼克、Gonzalez-Mina |

## 检索架构

单分类可达 282 条 / 5 万字符——整读≈3-4 万 token 只为挑 1-2 条。所以做成**真两级**：

```
路由总表  references/_index/_route.md                  全库 10 分类 × 74 簇，~6K 字符（LLM 判断入口）
一级索引  references/_index/<分类>.md                   该分类的簇表，~1K 字符
二级索引  references/_index/clusters/<分类>/NN-簇.md     簇内条目行，中位 2.8K 字符
```

**路径**：安全门 → 定月龄 → 读 `_route.md` 按理解判「分类 · 簇」（可列 2 候选）→ 读簇子索引双通道匹配 → 读 1-2 条条目全文 → 按输出骨架作答。簇内无命中则换同分类兄弟簇、再跨分类兜底。

索引与路由总表都由 `rebuild_index.py` 从条目 frontmatter 自动生成，簇规则集中在脚本里。

## 安装

与运行环境无关（只依赖「读文件 + 按协议作答」），两个入口任选或都装：

```bash
# Claude Code
cp -r baby-tutor ~/.claude/skills/baby-tutor

# Codex
cp -r baby-tutor ~/.codex/skills/baby-tutor
```

## 生产端 · baby-distill

知识库不是搜出来的，是从权威书**原文实文**蒸馏的。生产端是 `skills/baby-distill/`：

- `references/format.md`：条目格式标准——15 字段 + 13 节 + 鸡汤过滤器（机制/步骤/判断标准/红线 四件套缺一不收录）
- 源质量门 A/B/C/D 分级；扫描件走**视觉蒸馏协议**（逐页视觉读、看不清就舍弃、双读校验）
- 一书一 subagent 并行蒸馏；蒸馏代理只写条目，索引由主会话统一重建（并行安全）
- 医学数字双源核对官方指南

批次完成后必跑：

```bash
python skills/baby-distill/scripts/rebuild_index.py     # 重建两级索引 + 路由总表
python skills/baby-distill/scripts/validate_entries.py  # 机械验收（退出码非 0 = 有硬伤）
```

## 目录结构

```
baby-tutor/
├── SKILL.md                      # 消费端 skill（安全门 / 路由 / 输出骨架）
├── references/                   # 知识库
│   ├── _index/                   # _route.md 路由总表 + 分类簇表 + clusters/ 二级子索引
│   └── 00-安全与就医红旗/ … 09-父母自身/
├── skills/
│   └── baby-distill/             # 生产端（蒸馏工具 + 格式规范 + 脚本）
└── tasks/                        # 建设计划、书单、下载清单
```

## 设计原则

- **安全永远第一**：红旗症状优先于一切方法论
- **月龄是第一路由维度**：方法强依赖月龄，未说月龄必问
- **策略优先于来源**：给家长的是清晰观点 + 可落地策略，来源压到末尾
- **证据分级不站队**：争议主题给默认推荐 + 说清各派适用家庭
- **不要鸡汤**：每条必须有机制（标证据强度）+ 步骤化实操 + 判断标准 + 红线
- **原书实文**：低质量源不参与蒸馏

## 边界

不做诊断、不给药物剂量。疾病类只做观察指导 / 家庭护理边界 / 就医阈值。

## License

MIT
