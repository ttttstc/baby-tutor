# baby-tutor · 科学育儿知识库与 Skill

面向 0-6 岁（当前重点 0-1 岁）的育儿方法论知识库 + Claude skill。宝宝当前 3 个月，按「权威书原书实文蒸馏」建设，安全优先、月龄路由、证据分级、拒绝鸡汤。

## 这是什么

一个 Claude Code skill（`SKILL.md` + `references/`），家长带着育儿困扰来提问时：
0. **安全筛查**——命中红旗症状（3月内发热/呼吸窘迫/脱水等）→ 只输出就医指导，跳过方法论
1. **定位月龄**——唯一必问项（8个月的夜醒和3岁的夜醒是两个问题）
2. **定分类**——10 类（睡眠/喂养/情绪/管教/发展/早教/自理/社交/父母自身/安全红旗）
3. **匹配条目**——双通道（用户会怎么问逐字命中 > 判断同一问题）
4. **输出**——主推方案 + 2-3 条备选（适用家庭/代价）+ 就医红线 + 证据等级

## 知识库现状

- **1731 条方法论条目**，10 分类
- 全部来自**原书实文蒸馏**（`extraction` 字段可溯源到书名+章节 / 官方 URL）
- **证据分级**：tier-1 机构指南 / tier-2 同行评议 / tier-3 专家专著 / tier-4 流行理念（争议已标注）
- 每条目 13 节正文（含「正常范围与个体差异」「就医红线」两节育儿特有内容）

| 分类 | 条数 | 主要来源 |
|---|---|---|
| 00-安全与就医红旗 | 282 | AAP 育儿百科、崔玉涛、裴洪岗、虾米妈咪、冀连梅、Science of Mom、官方指南 |
| 01-睡眠 | 186 | Precious Little Sleep、法伯、Weissbluth、Kassowitz、实用程序育儿法、小土大橙子、Mindell、Karp |
| 02-喂养与营养 | 233 | Satter、崔玉涛、Science of Mom、Eliot、BLW |
| 03-情绪与安抚 | 72 | Karp 5S、Hogg、RIE、Lieberman |
| 04-管教与边界 | 211 | 蒙氏、Siegel、Faber、Greene、Phelan、德雷克斯、Gordon、Karp |
| 05-发展与里程碑 | 262 | AAP、Eliot、崔玉涛、Lieberman、Wonder Weeks |
| 06-游戏与早教 | 205 | 蒙氏（3 本）、Dirksen、RIE、Eliot、Cohen、Hanscom、NurtureShock、Suskind |
| 07-生活自理与习惯 | 127 | AAP、Jana、蒙氏、Azrin-Foxx、Glowacki、Payne |
| 08-社交与分离 | 67 | Gonzalez-Mina、Fraiberg |
| 09-父母自身 | 86 | Mindell、佩里、雷诺、Oster、高普尼克、Gonzalez-Mina |

## 目录结构

```
baby-tutor/
├── SKILL.md                    # 主 skill（消费端）
├── references/                 # 知识库
│   ├── _index/                 # 两级索引：分类簇表 + clusters/ 二级子索引
│   ├── 00-安全与就医红旗/ … 09-父母自身/
├── skills/
│   └── baby-distill/           # 蒸馏 skill（生产端工具）
│       ├── SKILL.md
│       ├── references/format.md    # 条目格式规范
│       └── scripts/
│           ├── rebuild_index.py    # 从 frontmatter 重建索引
│           └── validate_entries.py # 机械验收
└── tasks/                      # 建设计划、书单、下载清单
```

## 安装

```bash
cp -r baby-tutor ~/.claude/skills/baby-tutor
```

## 蒸馏工具（baby-distill）

知识库不是搜索来的，是从权威书**原书实文**蒸馏的。流程见 `skills/baby-distill/SKILL.md`：
每本书一个 subagent，按 `references/format.md`（15 字段 + 13 节 + 鸡汤过滤器）切方法论条目，源质量门 A/B/C/D 分级（C 级读书笔记、D 级乱码一律拒收），医学数字双源核对官方指南。

批次完成后必跑：
```bash
python skills/baby-distill/scripts/rebuild_index.py    # 重建索引
python skills/baby-distill/scripts/validate_entries.py # 机械验收
```

## 设计原则

- **安全永远第一**：育儿错误建议有身体代价——红旗症状优先于一切方法论
- **月龄是第一路由维度**：方法高度依赖月龄，用户没说月龄必问
- **证据分级不站队**：争议主题（睡眠训练/亲密育儿 vs 行为法）各说各的证据，给默认推荐+对立面
- **不要鸡汤**：每条必须有机制（标证据强度）+ 步骤化实操 + 判断标准 + 红线；「正常范围」只做数据对照不做安抚
- **原书实文**：非原书/低质量源不参与蒸馏（盗版、读书笔记、OCR 乱码一律拒收）

## 边界

不做诊断、不给药物剂量。疾病类只做观察指导 / 家庭护理边界 / 就医阈值。

## License

MIT
