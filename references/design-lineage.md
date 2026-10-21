# Lineage · 设计来源

Craft 现在是总调度入口。与旧版原则提炼不同，三个原仓库的全部已跟踪文件原样保存在 `../upstream/`，包括正文、示例、参数、参考、脚本、素材、源码与许可证；只排除 Git 历史与未跟踪文件。

| 来源 | 固定版本前缀 | 本地快照 | 许可 |
| --- | --- | --- | --- |
| [Emil Kowalski Skills](https://github.com/emilkowalski/skills) | 2d22863 | `../upstream/feel/` | 见原仓库 LICENSE |
| [Impeccable](https://github.com/pbakaus/impeccable) | 374a0e179 | `../upstream/finish/` | 见原仓库 LICENSE、NOTICE.md |
| [Taste Skill](https://github.com/Leonxlnx/taste-skill) | 63aba5f | `../upstream/form/` | 见原仓库 LICENSE |

精确提交与逐文件校验记录在 [manifest.json](../upstream/manifest.json)。上游原文未做措辞修改；路径和使用环境的适配、冲突处理均放在 [AGENTS.md](../AGENTS.md)，不暗改来源文件。

## 自有部分

`SKILL.md`、`AGENTS.md`、`agents/openai.yaml` 和完整性校验脚本是 Craft 调度与封装部分；`references/` 保存自有补充。仓库仅维护当前版本，不包含旧版 Craft 留档。


旧版从 [Ant Design Skills](https://github.com/ant-design/antd-skill) 借鉴了按版本查证公开 API、按问题选择资料和工具、按组件场景验证的方式；本轮没有打包 Ant Design 仓库。TD 仍独立，未纳入 Craft。

## 原样保留不等于全部执行

上游包含不同工具的安装/插件配置、仓库开发规则与重复构建产物。它们保留用于完整溯源，不会全部成为当前任务指令。只执行选定技能的相关流程，并遵守实际任务授权。原脚本可能需要单独准备运行时、浏览器、依赖或二进制；本轮未自动安装或启动它们。
