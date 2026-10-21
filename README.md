# Craft

一个自包含的界面设计技能。以 `AGENTS.md` 统一调度三个模块，按任务加载完整指导、参考与工具。

| 模块 | 职责 |
| --- | --- |
| Form | 视觉方向、页面构图、内容与素材组织 |
| Feel | 组件交互、动画、操作手感与性能 |
| Finish | 设计工作流、精修、评审与质量检查 |

## 安装

将本仓库克隆到 Codex 的技能目录。若已有同名目录，先确认其中的自定义修改，勿直接覆盖。

```bash
git clone https://github.com/Andreaaaaaaaa/craft.git ~/.codex/skills/craft
```

仓库为私有时，需具备仓库访问权限。整个目录可以复制使用，不依赖本机其他仓库或外部绝对路径。原工具所需的 Node、浏览器或二进制需按所选流程准备。

## 使用

在支持本地技能的环境中调用：

```text
使用 $craft，为我的产品设计一个登录页。
使用 $craft，检查并打磨这个表单的交互。
使用 $craft，评审当前页面，不修改代码。
```

入口为 `SKILL.md`，完整调度规则为 `AGENTS.md`。一次选定一个主流程，再按需加载辅助模块，无需分别安装三个模块。

## 目录

```text
craft/
├── SKILL.md
├── AGENTS.md
├── agents/
├── references/
├── scripts/verify-upstream.py
└── upstream/
    ├── form/
    ├── feel/
    ├── finish/
    └── manifest.json
```

TD 设计还原技能独立维护，不包含在本仓库中。本仓库只维护当前版本，不包含旧版 Craft 留档。

## 验证

```bash
python3 scripts/verify-upstream.py
```

校验固定来源内容的完整性，不代表所有工具已安装或所有设计流程已经实测。来源及许可见 `references/design-lineage.md` 和各来源目录中的原始记录。
