# baby-tutor 蒸馏书单总库 v1

> 生成：2026-10-03。三路联网检索合并去重（英文权威榜单 / 豆瓣直接抓取验证 / GitHub 开源资源），交叉我的知识库经典书。
> 用途：baby-tutor skill 的蒸馏来源登记表。条目 sources 字段引用本表 id。
> 优先级图例：**P0**（0-6月，本期蒸馏）｜**P1**（6-12月）｜**P2**（1-3岁）｜**P3**（3-6岁）｜**底座**（机制参考，不单独出条目）｜**澄清**（澄清条目素材）｜**备选**｜**不蒸馏**｜⚠️（警示/批判使用）

## 检索方法与可信度

- **英文**：agent-reach/Exa 全网语义搜索约 25 轮，覆盖 AAP/Mayo/CHOP/ZERO TO THREE/Forbes Vetted/Sleep Foundation/RIE.org/NAP 等来源。书名、作者、版次均经出版方页面验证，无虚构。
- **中文**：豆瓣图书页直接抓取（235 本入库）+ Brave 快照交叉。评级 A（豆瓣直抓）/ B（Brave 快照含星级分布）/ C（第三方转述，已标注）。未查到评分的明确标注，不虚构。
- **GitHub**：gh CLI 20+ 轮搜索，star 数为 2026-10-03 API 实测。
- 内置 WebSearch 本环境返回空，未使用；以上均由子代理经 agent-reach 完成。

---

## 一、双焦点 A：蒙台梭利（前缀 mon-）

| 书 | 作者（身份） | 验证 | 年龄 | 价值 | 蒸馏期 |
|---|---|---|---|---|---|
| Montessori: The Science Behind the Genius | Angeline Stoll Lillard（UVA 发展心理学教授） | 学界公认蒙氏实证检验专著 | 0-12岁 | 逐条检验蒙氏八大原理的实证证据——科学蒸馏蒙氏的标尺 | **P0·蒙氏证据层** |
| Montessori from the Start | Paula Lillard & Lynn Jessen（AMI 正统，Forest Bluff 创办人） | PRH 出版 | 0-3岁 | 蒙氏理念家庭环境正统落地（含 0-6 月移动区/吊饰/低床） | **P0** |
| The Montessori Baby | Simone Davies & Junnifa Uzodike（AMI 教师） | Workman 2021 | 0-1岁 | 蒙氏婴儿版——与当前月龄最匹配的应用书 | **P0** |
| The Montessori Toddler | Simone Davies（AMI） | 销量 20 万+，Forbes 2024 | 1-3岁 | 可操作的蒙氏家庭实践 | P2 |
| 童年的秘密 | 蒙台梭利（原著） | [豆瓣 8.3（816人）](https://book.douban.com/subject/34917698/) | 0-6岁 | 原始理论文本 | 底座 |
| 吸收性心智 | 蒙台梭利（原著） | 中文版评分未核实 | 0-6岁 | 原始理论（"吸收性心智"按理论假说标注） | 底座 |
| 蒙台梭利教育法 | 蒙台梭利（译本） | [豆瓣 8.7（49人）](https://m.douban.com/book/subject/3215776/) | 0-6岁 | 高分中文译本 | 底座·备选 |
| 爱和自由 | 孙瑞雪（本土蒙氏实践者） | [豆瓣 8.6（1233人）](https://book.douban.com/subject/1168575/) | 0-6岁 | 本土蒙氏实践观 | P2·对照 |
| 捕捉儿童敏感期 | 孙瑞雪 | [豆瓣 8.1（2575人）](https://book.douban.com/subject/24706978/) | 0-10岁 | 200 个敏感期真实案例——敏感期澄清条目的第一素材（其绝对化表述需实证对照） | P2·**澄清** |

## 二、双焦点 B：崔玉涛（前缀 cui-）

| 书 | 验证 | 年龄 | 价值 | 蒸馏期 |
|---|---|---|---|---|
| 崔玉涛育儿百科（2018） | [豆瓣 8.6（1127人）](https://book.douban.com/subject/30399656/) | 0-6岁 | 按月龄本土育儿全书，健康侧主力 | **P0·主力** |
| 崔玉涛图解家庭育儿（10 册，2012-15） | [各分册 7.9-8.4](https://book.douban.com/subject/11520909/) | 0-3岁 | 主题分册：发热/喂养/肠道/过敏/疫苗/生长发育/就医误区 | **P0·按主题取用** |
| 崔玉涛自然养育法（2021） | [豆瓣 8.0（1207人）](https://book.douban.com/subject/35553434/) | 0-6岁 | 65 案例 31 个常见养育误区 | **P0-P1** |
| 崔玉涛：宝贝健康公开课（2013） | [豆瓣 8.3（701人）](https://book.douban.com/subject/24318989/) | 0-3岁 | 早期科普合集，与上重叠 | 备选 |
| （BabyForge 已有）崔玉涛 5 阶段专栏 + 1-12 月逐月指导 | BabyForge cuiParenting.js | 0-12月 | 已蒸馏素材直接迁移 | **P0·迁移** |

> 科学性处理：与 AAP/WHO/卫健委冲突处以机构指南为准并标注；商业关联推荐（益生菌产品等）降权。

## 三、权威机构综合指南

| 书 | 作者 | 验证 | 年龄 | 蒸馏期 |
|---|---|---|---|---|
| 美国儿科学会育儿百科（Caring for Your Baby and Young Child） | AAP（Tanya Altmann 主编） | [豆瓣 9.2（1088人）](https://book.douban.com/subject/35218443/)；第8版 2026 | 0-5岁 | **P0·事实基准** |
| Your Baby's First Year | AAP | 第6版 2025，销量 400 万+ | 0-1岁 | **P0** |
| 美国儿科学会健康育儿指南 | AAP（谢尔弗主编） | [豆瓣 9.1（37人）](https://book.douban.com/subject/26997339/) | 0-12岁 | **P0**（00 类症状流决策） |
| 梅奥育儿全书 | Mayo Clinic | [豆瓣 9.0（146人）](https://book.douban.com/subject/27053674/) | 0-3岁 | **P0·交叉验证** |
| Heading Home With Your Newborn | Laura Jana & Jennifer Shu（儿科医生） | AAP 出版，第5版 2025 | 0-3月 | **P0**（出院回家实操，正当月龄） |
| 定本育儿百科 | 松田道雄（日本儿科医生） | [豆瓣 8.5（1955人）](https://book.douban.com/subject/1101921/) | 0-6岁 | 备选（2002 年版，需时效警示） |
| 斯波克育儿经 | Benjamin Spock（第10版 Needlman 修订） | [豆瓣 8.2（588人）](https://book.douban.com/subject/2276901/) | 0-18岁 | 不主蒸（历史地位，医学内容过时） |
| 西尔斯亲密育儿百科 | William Sears | [豆瓣 8.4（3207人）](https://book.douban.com/subject/4177120/) | 0-2岁 | **澄清/对立参考**（流派立场，实证弱） |
| Baby 411 / Toddler 411 | Ari Brown（儿科医生） | Boston Children's 书单，销量 100 万+ | 0-4岁 | 备选（P1+） |
| Moms on Call: 0-6 Months | Hunter & Walker（儿科护士） | Parents 2026 奖 | 0-6月 | **P0·对照**（偏刚性一端，与 Possums 形成谱系） |
| 首儿所育儿百科（2023） | 首都儿科研究所 60 名专家 | 六部门科普图书奖 | 0-12岁 | 备选（本土权威） |
| 0-6岁小儿养育手册（第三版） | 上海市儿童医院 | 上海科技出版社 2021 | 0-6岁 | 备选 |
| 丁香妈妈科学养育 | 丁香园百位医生 | 得到引 8.3（C级） | 0-3岁 | 备选 |

## 四、睡眠（前缀 slp-）

| 书 | 作者 | 验证 | 年龄 | 蒸馏期 |
|---|---|---|---|---|
| Solve Your Child's Sleep Problems | Richard Ferber（波士顿儿童医院睡眠中心创始人） | Sleep Foundation/babysleepscience | 0-学龄 | **P1**（渐进消退，RCT 支持最强；P0 建框架） |
| Healthy Sleep Habits, Happy Child | Marc Weissbluth（西北大学儿科教授） | babysleepscience | 0-青春期 | **P0·机制层**（睡眠压力/早睡；注意：中文版《婴幼儿睡眠圣经》[豆瓣 6.5（318人）](https://book.douban.com/subject/6509769/)争议大，引用理念并标注） |
| Precious Little Sleep | Alexis Dubief（独立睡眠研究者） | Forbes 2024 睡眠类最佳；Callahan 推荐 | 0-3岁 | **P0-P1**（证据密度高，当代口碑第一梯队） |
| The Discontented Little Baby Book | Pamela Douglas（澳洲 GP，Possums 创始人） | Possums 官方 | 0-6月 | **P0**（循证反过度作息，柔性一端） |
| 实用程序育儿法 | Tracy Hogg（Baby Whisperer） | [豆瓣 8.4（187人）](https://book.douban.com/subject/3420221/) | 0-2岁 | **P0**（E.A.S.Y. 锚点） |
| 每个孩子都能好好睡觉 | 莫根罗特（德国儿科医生） | [豆瓣 8.6（90人）](https://book.douban.com/subject/4876945/) | 0-6岁 | P0·备选 |
| The Happy Sleeper | Turgeon & Wright（MFT） | 10 万+家庭 | 0-学龄 | P1（Sleep Wave 温和法） |
| Sleeping Through the Night | Jodi Mindell（CHOP 睡眠中心副主任） | CHOP 官方 | 0-3岁 | P1（学术最硬之一） |
| The No-Cry Sleep Solution | Elizabeth Pantley | Sleep Foundation | 0-2岁 | P1·**对立条目**（⚠️ 无医学背景，部分主张与安全睡眠建议冲突，批判使用） |
| 婴幼儿睡眠全书 | 小土大橙子 | 口碑强，豆瓣评分未核实 | 0-2岁 | P1·备选（中文实操参考） |
| ⚠️ On Becoming Babywise / 12 Hours by 12 Weeks | Ezzo / Giordano | babysleepscience 明确不推荐 | — | **警示条目**（刚性作息风险） |

## 五、喂养与营养（前缀 feed-）

| 书 | 作者 | 验证 | 年龄 | 蒸馏期 |
|---|---|---|---|---|
| Child of Mine / Feeding with Love and Good Sense（First Two Years 分册） | Ellyn Satter（RD，DOR 创立者） | ESI 官方 | 0-6岁 | **P0**（0-6月部分）+ P1（分工完整版） |
| 母乳喂养的女性艺术 | 国际母乳会 LLLI | [豆瓣 8.4（85人）](https://book.douban.com/subject/30286036/) | 0-2岁 | **P0** |
| The Science of Mom | Alice Callahan（营养科学博士） | Johns Hopkins UP 第2版 | 0-1岁 | **P0**（逐主题循证审读） |
| Baby-Led Weaning | Gill Rapley（BLW 创立者） | The Experiment | 6月-1岁 | P1 |
| Solid Starts | Solid Starts 多学科团队 | 2025 | 6月-2岁 | P1（呛噎防护+过敏预防） |
| Baby Leads the Way | Julie Laux 等，AAP 出版 | 2024/25 | 6-12月 | P1（AAP 官方辅食指南） |
| 辅食每周吃什么 | 刘长伟（营养师） | 豆瓣评分未核实 | 6月+ | P1·备选 |
| What to Feed Your Baby | Tanya Altmann（儿科医生） | AAP 主编 | 辅食期 | 备选 |
| 每个孩子都能好好吃饭 | 德国系 | 评分未核实 | 1-6岁 | P2·备选 |

## 六、发展心理学与脑科学（前缀 dev-，机制底座）

| 书 | 作者 | 验证 | 年龄 | 蒸馏期 |
|---|---|---|---|---|
| Development Through the Lifespan | Laura Berk（教授） | SAGE 第7版 2022 | 全生命周期 | **底座** |
| 从出生到3岁 | Burton White（哈佛学前项目总负责人） | [豆瓣 8.4（1237人）](https://book.douban.com/subject/1967845/) | 0-3岁 | **P0**（七阶段发展指南） |
| 婴幼儿及其照料者（第8版） | Gonzalez-Mina & Eyer（幼教专家） | 商务印书馆 2016 | 0-3岁 | **P0·底座**（尊重回应式保育教科书，03 类+照护机制） |
| Touchpoints: Birth to Three | Brazelton & Sparrow（哈佛） | Brazelton Touchpoints Center | 0-3岁 | P0-P1（触点理论：飞跃前的混乱是正常窗口） |
| What's Going on in There? | Lise Eliot（神经科学家） | PRH | 孕-5岁 | **底座**（脑发育全图谱） |
| 魔法岁月 | Selma Fraiberg（儿童精神分析） | [豆瓣 8.8（984人）](https://book.douban.com/subject/26352480/) | 0-6岁 | 底座（18月+ 部分 P2 出条目） |
| 园丁与木匠 | Alison Gopnik（伯克利） | [豆瓣 8.1-8.3](https://book.douban.com/subject/34481379/) | 全年龄 | 底座注记 |
| From Neurons to Neighborhoods | Shonkoff & Phillips（美国国家研究委员会） | NAP 2000 | 0-5岁 | **底座**（学术基石，引用级） |
| The Wonder Weeks | van de Rijt & Plooij | 官方网站 | 0-20月 | P0-P1·⚠️ tier-4（"心智飞跃"预测方法学受批评，标注使用） |
| 养育的选择 | 陈忻（美国儿童发展心理学博士） | [豆瓣 8.8（CSDN 引用）](https://book.douban.com/subject/26797268/) | 0-8岁 | **P0·澄清素材**（13 个中国家长迷思：敏感期/早教/规则） |
| NurtureShock（教养大震撼） | Bronson & Merryman | NYT 畅销 6 个月+ | 3-14岁 | **澄清素材**（睡眠/表扬/自控反直觉研究） |
| 父母的语言（Thirty Million Words） | Dana Suskind（芝加哥大学外科医生） | [中文版豆瓣 7.0+](https://book.douban.com/subject/32875410/)（未核实）；Penguin | 0-3岁 | **澄清条目**（3T 原则保留；3000万词汇差距已被方法学质疑） |
| Einstein Never Used Flash Cards | Hirsh-Pasek & Golinkoff（发展心理学教授） | 修订 2023 | 0-9岁 | P2（自由游戏论证） |
| 让孩子的大脑自由 | John Medina | [豆瓣 8.5（950人）](https://book.douban.com/subject/10758030/) | 0-5岁 | 备选（与 Eliot 重叠，辟谣条目可用） |
| 读懂孩子（0-6岁） | 边玉芳（北师大教授） | [豆瓣 7.6（40人）](https://book.douban.com/subject/25879741/) | 0-6岁 | 备选 |
| 0-3岁儿童最佳的人生开端 | 鲍秀兰（协和儿科教授） | [豆瓣 8.0（46人）](https://m.douban.com/book/subject/1277498/) | 0-3岁 | 备选 |
| 教出乐观的孩子 | 塞利格曼 | 豆瓣 7.9 | 学龄期 | P3·备选 |
| Gesell 年龄系列（Your One-Year-Old 等） | Ames & Ilg（Gesell 研究所） | Penguin | 1-14岁 | P2·备选（按年龄行为画像） |
| The Emotional Life of the Toddler | Alicia Lieberman（UCSF） | ZERO TO THREE 推荐 | 1-3岁 | P2 |

## 七、情绪安抚（前缀 sooth-）

| 书 | 作者 | 验证 | 年龄 | 蒸馏期 |
|---|---|---|---|---|
| The Happiest Baby on the Block | Harvey Karp（儿科医生） | Goodreads 3.89（3.2万人）；百万销量 | 0-6月 | **P0**（5S 安抚法；"第四孕期"标注为假说） |
| Raising Your Spirited Child | Kurcinka | 100 万+册 | 0-10岁 | P2·备选（高需求儿童） |

## 八、管教与沟通（前缀 04 类，P2-P3）

| 书 | 作者 | 验证 | 年龄 | 蒸馏期 |
|---|---|---|---|---|
| 正面管教（含 0-3岁/3-6岁分龄版） | Jane Nelsen | [豆瓣 8.7（9006人）](https://book.douban.com/subject/3420606/)；0-3岁分册 8.3（758人） | 2-18岁 | **P2** |
| 如何说孩子才会听 | Faber & Mazlish | [豆瓣 8.8（4975人）](https://book.douban.com/subject/2275635/) | 2-12岁 | **P2** |
| How to Talk So Little Kids Will Listen | Joanna Faber & Julie King | Kirkus 星级 | 2-7岁 | P2（更落地的幼儿版） |
| 孩子：挑战 | 德雷克斯（阿德勒学派） | [豆瓣 9.1（3752人）](https://book.douban.com/subject/26304087/) | 2-18岁 | **P2**（阿德勒基础，正面管教源头） |
| 父母效能训练 P.E.T. | Thomas Gordon | [豆瓣 9.0（1890人）](https://book.douban.com/subject/26681417/) | 全年龄 | P2-P3·备选（我-信息/积极倾听技术） |
| No-Drama Discipline（去情绪化管教） | Siegel & Bryson | NYT 畅销 | 1-10岁 | P2 |
| No Bad Kids | Janet Lansbury（RIE） | Bryson 背书 | 1-3岁 | **P2** |
| The Explosive Child（暴脾气小孩） | Ross Greene（CPS 循证模型） | livesinthebalance 标注 evidence-based | 3-12岁 | P3（技能不足范式） |
| 1-2-3 Magic | Thomas Phelan | **有 RCT 验证**（2014 澳洲，效果 2 年） | 2-12岁 | P2-P3 |
| Peaceful Parent, Happy Kids（平和式教养法） | Laura Markham | Forbes 2024 | 0-9岁 | P2·备选 |
| 全脑教养法 | Siegel & Bryson | [豆瓣 8.3（1144人）](https://book.douban.com/subject/22224887/) | 2-12岁 | P2·**策略层**（脑科学表述按批评修正注记） |
| 游戏力 | Lawrence Cohen | [豆瓣 8.5（2312人）](https://book.douban.com/subject/6084402/) | 0-12岁 | P2·备选（蒸馏时判定策略含量） |
| 看见孩子（Good Inside） | Becky Kennedy | [豆瓣 9.2（2823人）](https://book.douban.com/subject/36427596/) | 0-10岁 | 备选（豆瓣极高但治愈系为主；仅提取"归因良好意图"等具体策略） |
| 孩子，把你的手给我 | Haim Ginott | 豆瓣 8.8（C级） | 2-12岁 | P2·备选（沟通技术源头） |
| 你就是孩子最好的玩具 | 金伯莉·布雷恩 | [豆瓣 8.1（2704人）](https://book.douban.com/subject/6759256/) | 0-7岁 | 备选 |
| Raising Human Beings | Ross Greene | Guilford | 学龄 | P3·备选 |
| Tiny Humans, Big Emotions / The Tantrum Survival Guide | Campbell & Stauble / Hershberg | Forbes 2024 / Guilford | 0-6岁 | 备选 |
| 管教啊，管教 | 汪培珽 | [豆瓣 8.2（133人）](https://book.douban.com/subject/4747184/) | 2-6岁 | 备选 |
| 不管教的勇气 | 岸见一郎 | 豆瓣 8.3（C级） | 学龄 | 不蒸馏 |

## 九、教育流派（RIE/瑞吉欧/华德福/自然，前缀 06/08 类）

| 书 | 作者 | 验证 | 年龄 | 蒸馏期 |
|---|---|---|---|---|
| Your Self-Confident Baby | Magda Gerber（RIE 创始人） | RIE.org 官方推荐 | 0-2岁 | **P0-P1**（尊重式照护原典，与蒙氏互补） |
| Dear Parent | Magda Gerber | RIE.org 指定教材 | 0-2岁 | 备选 |
| Baby Knows Best | Deborah Solomon（前 RIE 执行总监） | Hachette | 0-2岁 | 备选 |
| Elevating Child Care | Janet Lansbury | RIE | 0-2岁 | P1·备选 |
| The Hundred Languages of Children | Edwards & Gandini（编） | Reggio Children 官方 | 0-6岁 | P3·参考（机构教学法，家庭应用低） |
| Simplicity Parenting | Kim John Payne（华德福背景） | Hallowell 推荐 | 0-12岁 | P2·备选（环境/节奏/日程简化有操作层） |
| Balanced and Barefoot | Angela Hanscom（儿科作业治疗师） | Peter Gray 推荐 | 0-12岁 | P2-P3（户外与感统） |
| 好妈妈胜过好老师 | 尹建莉 | [豆瓣 8.9（12562人）](https://book.douban.com/subject/3465080/) | 0-18岁 | P2·备选（中国案例，挑操作性内容） |
| Hunt, Gather, Parent | Michaeleen Doucleff（NPR 科学记者） | NYT 书评 | 0-6岁 | 备选 |
| Screen Time / Into the Minds of Babes | Lisa Guernsey | 学界广泛引用（3C 框架） | 0-5岁 | P3（屏幕条目） |

## 十、数据驱动/循证判读

| 书 | 作者 | 验证 | 年龄 | 蒸馏期 |
|---|---|---|---|---|
| Cribsheet | Emily Oster（布朗经济学教授） | The Atlantic 书评 | 0-学前 | **P0·判读范式**（证据分级怎么读；⚠️ 儿科学界对其哺乳等结论有保留，标注使用） |
| The Informed Parent | Haelle & Willingham | Paul Offit 推荐 | 0-4岁 | 备选 |
| The Family Firm | Emily Oster | — | 学龄前 | P3·备选 |

## 十一、中国医生健康类（前缀 00 类主力）

| 书 | 作者 | 验证 | 年龄 | 蒸馏期 |
|---|---|---|---|---|
| 崔玉涛系（见双焦点 B） | — | — | — | **P0·主力** |
| 在孩子下次生病前 | 裴洪岗（儿科医生） | [豆瓣 8.4](https://book.douban.com/subject/34783026/) | 0-6岁 | **P0**（循证：生病时怎么判断与应对） |
| 冀连梅谈：中国人应该这样用药（图解母婴版） | 冀连梅（药师） | [豆瓣 9.1（292人）](https://book.douban.com/subject/26760489/) | 孕-6岁 | **P0·参考**（用药安全边界与家庭药箱误区；不给剂量的纪律不变） |
| 虾米妈咪育儿正典 | 余高妍（儿科医生妈妈） | [豆瓣 8.2（304人）](https://book.douban.com/subject/25909417/) | 0-3岁 | P0·备选 |
| 郑玉巧育儿经·婴儿卷 | 郑玉巧 | [豆瓣 8.2（438人）](https://book.douban.com/subject/3241963/) | 0-1岁 | 备选（与崔重叠） |
| 西尔斯健康育儿百科 | 西尔斯 | [豆瓣 8.4（255人）](https://book.douban.com/subject/26373220/) | 0-12岁 | 备选（A-Z 症状，与 AAP 指南重叠） |
| 张思莱科学育儿全典 | 张思莱 | [豆瓣 7.7（55人）](https://book.douban.com/subject/27069725/) | 0-3岁 | 不主蒸（评分一般） |
| 像我这样做妈妈 | 欧茜（儿科医生） | 口碑，评分未核实 | 0-3岁 | 备选 |

## 十二、父母自身（前缀 par-）

| 书 | 作者 | 验证 | 年龄 | 蒸馏期 |
|---|---|---|---|---|
| 真希望我父母读过这本书 | 菲利帕·佩里（英国心理治疗师） | [豆瓣 8.7-8.8](https://book.douban.com/subject/35173329/)（C级） | 全年龄 | **P0·备选**（代际传递，机制条目） |
| 不吼不叫 | 罗娜·雷纳 | 豆瓣 8.0-8.3（C级） | 0-12岁 | P0·备选（ABCDE 情绪法则） |
| 反思的爱 | 雷吉娜·帕利（精神病学家） | [豆瓣 8.9（106人）](https://book.douban.com/subject/33402528/) | 0-18岁 | 备选（心智化，偏专业） |
| Self-Compassion for Parents | Susan Pollak | Guilford | — | 备选 |
| 我当妈妈了，还是我自己 | （未检索） | — | — | 待补 |

## 十三、官方指南与机构文件（国标基线，网络校准源）

| 文件 | 机构 | 年份 | 用途 |
|---|---|---|---|
| 3岁以下婴幼儿健康养育照护指南（试行） | 国家卫健委 | 2022 | 国内基准线，gov.cn 可查 |
| 婴幼儿早期发展服务指南 / 营养喂养评估服务指南（试行） | 国家卫健委 | 2025 | 新一批官方指南 |
| AAP 安全睡眠立场（Back to Sleep/SSD） | AAP | 持续更新 | 00/01 类校准源 |
| AAP 屏幕/喂养立场文件 | AAP | 持续更新 | 06 类校准源 |
| WHO 生长标准 | WHO | — | 数据层（不复制，查证用） |
| 儿心量表-II | 中国 | — | 发育评估数据层（GitHub 有开源版） |

## 十四、警示名单（⚠️ 收录即批判/仅作反面）

| 书 | 问题 |
|---|---|
| On Becoming Babywise（Ezzo） | babysleepscience 明确不推荐：刚性喂养-作息有风险 |
| 12 Hours of Sleep by 12 Weeks（Giordano） | 同上 |
| 婴幼儿睡眠圣经（Weissbluth 中文版） | 豆瓣 6.5，哭声免疫倾向争议大——Weissbluth 机制层引用，操作层批判 |
| No-Cry Sleep Solution（Pantley） | 无医学背景，部分主张与安全睡眠冲突 |
| 斯波克育儿经（老版） | 首版 1946，医学内容过时（第10版部分修订） |
| 定本育儿百科 | 2002 年版，日本国情+时效问题 |
| 西尔斯亲密育儿（部分主张） | 同睡安全等主张与 AAP 立场冲突，流派立场标注 |

## 十五、GitHub 开源资源（借鉴与数据，不直接抄）

| 仓库 | Star | 价值 |
|---|---|---|
| [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | ~35.9k | 证据分级+期刊溯源的条目范式（含育儿章节）——条目格式参考 |
| [babybuddy/babybuddy](https://github.com/babybuddy/babybuddy) | ~2.9k | 育儿追踪事实标准（产品形态参考） |
| [pythias/NewParent](https://github.com/pythias/NewParent) | ~162 | 中文育儿攻略站（星数最高的纯育儿知识库）——分类学参考 |
| [cuipengfei/cyt](https://github.com/cuipengfei/cyt) | ~1 | **《崔玉涛育儿百科》PDF 转 Markdown**——崔玉涛蒸馏的直接素材源 |
| [MJorgin/yuer-triage](https://github.com/MJorgin/yuer-triage) | ~2 | 崔玉涛/段涛/叶盛等名医立场蒸馏先例 |
| [elya55/yuer](https://github.com/elya55/yuer) | 0 | 33 本顶级育儿书提炼 AI 助手——同构项目 |
| [mitoly/noob-dad](https://github.com/mitoly/noob-dad) | 0 | 13 阶段+8 专题 300+ 检查项（注明国家规范出处） |
| [hub2333/baby-wiki-doc](https://github.com/hub2333/baby-wiki-doc) | 0 | Obsidian 双链育儿知识库（含来源索引） |
| [Si1ence0591/child-assessment](https://github.com/Si1ence0591/child-assessment) | 0 | 儿心量表-II 数据——05 类发育对照数据源 |
| [UNICEFECAR/parenting-app-bebbo-mobile](https://github.com/UNICEFECAR/parenting-app-bebbo-mobile) | ~18 | UNICEF 官方育儿 App 内容——权威开源内容 |
| [GreenDou/toddler-curriculum](https://github.com/GreenDou/toddler-curriculum) | 0 | WHO/CDC/AAP+蒙氏/Pikler/HighScope 融合课程 |
| [junlintu/montessori-elementary-vault](https://github.com/junlintu/montessori-elementary-vault) | 0 | 蒙氏全学科知识库（小学段） |
| [qtttttttttting/toddler-guide](https://github.com/qtttttttttting/toddler-guide) | 0 | 蒙氏 18-36 月家庭教育指南 |
| [forumdata-collab/montessori-sensitive-periods-gantt](https://github.com/forumdata-collab/montessori-sensitive-periods-gantt) | 0 | 蒙氏敏感期甘特图——敏感期澄清条目可视化素材 |
| [SquirtleHankes/super-daddy](https://github.com/SquirtleHankes/super-daddy) | ~8 | WHO/AAP 12 模块育儿 Skill（references 结构同类先例） |
| [rcpch/digital-growth-charts-server](https://github.com/rcpch/digital-growth-charts-server) | ~16 | 皇家儿科医学院生长曲线 API |
| [dqsis/child-growth-charts](https://github.com/dqsis/child-growth-charts) | ~37 | WHO 生长标准 LMS 数据实现 |

## 十六、扩展候选（已验证存在，暂不排期）

英文：Raising a Secure Child（Circle of Security, Guilford）｜The Power of Showing Up（Siegel 4S 依恋框架）｜The Scientist in the Crib（Gopnik）｜Brain Rules for Baby｜Mind in the Making｜How Toddlers Thrive（Tovah Klein）｜How Children Succeed｜First Bites｜French Kids Eat Everything｜What to Expect the First Year（商业成功但专家评价低于 AAP 系）｜Dad to Dad / The New Father（父亲视角）｜Becoming the Parent You Want to Be｜Advanced Parenting（特殊需求）｜The Evolved Nest｜Toilet Training in Less Than a Day（Azrin & Foxx, 1974）｜The Happiest Toddler（Karp, Toddler-ese）

中文：谁拿走了孩子的幸福（李跃儿）｜当我遇见一个人（李雪，"母婴关系决定一切关系"——⚠️ 理念绝对化需对照）｜喂故事书长大的孩子（汪培珽）｜让孩子做主（小巫）｜骑鲸之旅（粲然）｜窗边的小豆豆（叙事，不蒸馏）｜夏山学校（理念叙事，不蒸馏）｜爱和自由续作｜西尔斯橙色亲子课（高需求宝宝）｜自驱型成长（学龄后）｜故事知道怎么办

## 统计与 P0 蒸馏规模

- 总库：约 115 本（双焦点 14 + 综合 13 + 睡眠 11 + 喂养 9 + 发展 19 + 安抚 2 + 管教 18 + 流派 10 + 判读 3 + 健康类 8 + 父母 4 + 官方 6）+ GitHub 17 仓库 + 扩展候选 30+
- **P0 本期蒸馏（0-6 月）**：约 25 本书 → 55-65 条条目（双焦点 20-28 条 + 睡眠/喂养/安抚/发展/安全/父母）
- P1 约 12 本、P2 约 18 本、P3 约 8 本，随月龄推进开工前重估
