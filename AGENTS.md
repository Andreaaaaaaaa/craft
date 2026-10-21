# Craft · 总调度规则

本文件是 `$craft` 的调度入口。所有相对路径从本文件所在的 Craft 目录解析。它控制本技能如何使用三个完整上游，不是用户项目根目录的 AGENTS.md，也不覆盖项目自身的约束。

## 1. 内容保留与读取

Craft 是自包含目录。三个原技能及其工具、素材都位于本目录的 `upstream/`，不依赖其他位置的仓库副本，也不要求另行安装三个技能。复制整个 Craft 文件夹即可保留调度所需资料。只按下列明确入口读取当前任务所需文件，不递归加载整个目录；许可、版权、发布资料和来源清单仅在相关任务中读取。

`upstream/` 保存三个仓库在固定提交上的全部已跟踪文件，包括原始技能、参考、参数、示例、脚本、素材、源码和许可证；不包含 Git 历史、未跟踪文件或未提供的运行时产物。不要把原技能压缩成几条原则后声称已使用它。

先选任务主流程，完整读取对应的 SKILL.md，再按其指引加载关联参考和工具。辅助技能在需要时读取。完整保留不等于每次全文加载，也不等于三个主流程同时执行。

上游仓库里的开发用 AGENTS.md、安装说明、插件配置与发布脚本也是保留的原始资料，不是对当前用户项目自动生效的指令。只有选定技能及所需参考承担当前任务指导；不要因为读取了仓库就执行安装或修改配置。

## 2. 核心入口

内部名称统一为 **Form / Feel / Finish**，分别来自 Taste / Emil Kowalski / Impeccable。下文出现的原作者名、原技能名及 CLI 命令用于定位原始内容，不是额外依赖或另一套模块。

| 模块 | 主入口 | 用途 |
| --- | --- | --- |
| Form · 视觉设计 | [SKILL.md](upstream/form/skills/taste-skill/SKILL.md) | 网页和产品界面的视觉方向、内容组织、方向库、素材、浏览器检查与迭代 |
| Finish · 质量打磨 | [SKILL.md](upstream/finish/.agents/skills/impeccable/SKILL.md) | 完整设计工作流，以及 shape、critique、audit、polish、harden、adapt、typeset 等原生命令与参考 |
| Feel · 交互工艺 | [emil-design-eng](upstream/feel/skills/emil-design-eng/SKILL.md) | 组件设计、交互手感、动效决策和细节；专项入口见下表 |

Impeccable 使用 `.agents/skills/impeccable/` 的 Codex 版本；同仓库的其他 provider 副本和 `skill/SKILL.src.md` 也保留，避免混用多个副本形成重复规则。

## 3. 按任务分工

- **新建网页、品牌页面、完整视觉改版**：默认 Form 主导。按它的页面或 app-screen 分流执行完整流程，包括所需方向库、内容、素材及 inspector；需要质量审计时再读取 Finish 对应命令，不在审计阶段重新开一次方向流程。
- **操作型界面与产品流程**：先识别用户任务。完整设计可走 Form 的 app-screen 流程；明确的 shape、onboard、harden 等请求走 Finish 对应 playbook。不能把营销页流程套到后台。
- **现有界面的精修、布局、字体、响应式或问题修复**：Finish 对应 playbook 主导，保留现有视觉依据。涉及组件手感时加载 Feel；除非任务要求重设计，不重新抽选 Form 视觉方向。
- **组件交互与动画实现**：Feel 对应专项主导；页面的已定方向保持不变。
- **视觉或技术评审**：Finish 的 critique / audit；动效评审走 Feel 的 review-animations。仅评审时保持只读，不能自行把发现变成修改任务。
- **用户明确指定原模块或命令**：优先使用对应入口。若请求包含多个独立目标，按阶段分配，不让三者同时争夺同一决定。
- **需求模糊**：只询问影响结果的关键信息；用户允许探索时明确说明假设。概念稿可以使用明确标识的虚构场景，不把自行编造的品牌和业务事实冒充用户需求。
- **TD / Figma 还原**：TD 保持独立。Craft 不打包、复制、替换或强制调用 TD。用户同时点名两者时，明确还原与设计改动各自范围，并遵守相应专用工具前置要求。

开始任务时用一句话说明本次主模块与辅助模块；无需把路由过程写成长计划。若用户仅调用 Craft 而无任务，询问目标，不自动初始化项目或运行命令。原技能的“仅首次无具体问题时问候”只适用于确实没有任务，不阻止已有请求的执行。

## 4. Feel 专项入口

按请求读取相应完整技能，保留它的适用范围、只读/实现区分、具体数值与示例。

| 任务 | 入口 |
| --- | --- |
| 组件与设计工程 | [emil-design-eng](upstream/feel/skills/emil-design-eng/SKILL.md) |
| 新建 Web 动画 | [animate](upstream/feel/skills/animate/SKILL.md) |
| 动画代码评审 | [review-animations](upstream/feel/skills/review-animations/SKILL.md) |
| 全项目动效审计与改进计划 | [improve-animations](upstream/feel/skills/improve-animations/SKILL.md) |
| 寻找适合增加动效的位置 | [find-animation-opportunities](upstream/feel/skills/find-animation-opportunities/SKILL.md) |
| 卡顿、合成与帧预算 | [animation-performance](upstream/feel/skills/animation-performance/SKILL.md) |
| 查询动效术语 | [animation-vocabulary](upstream/feel/skills/animation-vocabulary/SKILL.md) |
| Apple 设计、物理交互与手势 | [apple-design](upstream/feel/skills/apple-design/SKILL.md) |
| 移动 Web 与 PWA 手感 | [mobile-native](upstream/feel/skills/mobile-native/SKILL.md) |
| React Native / Expo 动画 | [animate-expo](upstream/feel/skills/animate-expo/SKILL.md) |
| Swift 代码与并发 | [write-swift](upstream/feel/skills/write-swift/SKILL.md) |
| Sonner toast | [ask-sonner](upstream/feel/skills/ask-sonner/SKILL.md) |
| 极端数据与边界测试 | [break-ui](upstream/feel/skills/break-ui/SKILL.md) |
| 多方案可切换原型，仅明确请求时 | [prototype](upstream/feel/skills/prototype/SKILL.md) |
| UI 库选型，仅明确请求时 | [pick-ui-library](upstream/feel/skills/pick-ui-library/SKILL.md) |

## 5. 冲突处理：范围优先，不改写原文

遵循系统与开发者指令、用户请求、项目适用规则；本文件只调度技能，不扩大权限。随后按“本次主模块负责的决定 → 专项模块负责的细节 → 辅助建议”执行。

- **方向与风格**：没有通用默认审美，主模块根据项目形成方向。选用 Taste 后遵守其完整方向选择、house rules 与 inspector；不能以“不固定审美”为由把它降为可忽略的建议。用户明确指定的品牌、风格与素材优先，发生具体冲突时局部说明适用例外，不整体废弃原流程。
- **动画**：动画专项由 Emil 决策，包括是否需要动画、时长、曲线、弹簧、打断和性能。Impeccable 的视觉审计不能仅因另一套通用偏好推翻已确定的交互机制；可访问性与实际性能问题仍应修复。
- **流程**：一次只运行一个主初始化/设计流程。辅助模块处理明确问题，不重新初始化、改写全部文档或建立第二份互相矛盾的方向。
- **输出格式**：执行 Emil 的代码评审时遵守其 Before / After / Why 表格要求；执行其他专项时遵守对应输出，不强制把所有结果改成 Craft 的统一模板。
- **保留细节**：不把上游数值、示例、反例和强约束静默改成泛泛原则。若实际项目需要偏离，说明具体冲突和采用的处理，以任务范围为限。

## 6. 工具与路径适配

令 `CRAFT_ROOT` 为本文件实际所在目录。以下均表示绝对路径替换，不依赖当前项目下安装原技能：

- Taste 的 `<skill>` = `CRAFT_ROOT/upstream/form/skills/taste-skill`。
- Impeccable 的 `<skill-base-dir>` = `CRAFT_ROOT/upstream/finish/.agents/skills/impeccable`。
- Emil 各项的基目录 = 对应 `SKILL.md` 所在目录。

执行脚本时保留原文要求的用户项目 cwd，让 `.taste-skill/`、`.impeccable/` 等工作产物落入对应项目，而不是修改原文快照。不要把路径占位符直接当作可执行字符串。

原脚本、资产和源码已保存，不代表浏览器、Node、二进制或依赖已安装。需要执行时检查实际依赖，使用对应原入口和工具；遇到缺失按上游明确的降级方案处理，披露未执行检查。不要用手写占位检查冒充原 inspector / detector 的结果。

不会因调用 Craft 自动安装插件、写全局 hooks、更新原仓库、发布内容或提交外部反馈。需要这些操作时按实际用户授权与当前环境规则执行。原文中的工具允许列表不赋予当前环境中不存在的工具或权限。

## 7. Craft 自有补充

以下文件提供补充指导，不替代三个原技能的完整内容：

- [art-direction.md](references/art-direction.md)：旧版视觉方向补充。
- [interaction-detail.md](references/interaction-detail.md)：旧版交互补充。
- [quality-review.md](references/quality-review.md)：版本/API 查证、组件场景验证和证据边界的补充。

第三方组件实现先确认项目版本、公开 API 与扩展接口；不确定时查本地类型或官方资料。按任务选表单、表格、上传、对话框等回归场景，不绑定 Ant Design 或强制安装 CLI。补充与选定上游冲突时按第 5 节处理，不用旧版摘要削弱原文。

## 8. 来源、更新与验证

[设计来源](references/design-lineage.md)记录原仓库及使用边界；[manifest.json](upstream/manifest.json)保存精确提交与每个文件的 SHA-256 或符号链接目标。

不自动跟随 main。需要更新时在独立位置准备新版本、对比原文变化与 Craft 路由，然后整体替换对应快照并更新清单，不覆盖用户自定义补充。

运行 `python3 scripts/verify-upstream.py`（相对 Craft 根目录）可校验快照完整性。该校验只证明文件保留与路由目标存在，不证明工具已可运行、视觉质量已通过或完整工作流已实测。
