# AI Native Video Architect

A modular Codex/Agent Skill for creating, transforming, diagnosing, and production-adapting AI-native video narratives.

## What is included

- Four modes: Create, Transform, Diagnose, Adapt
- Core AI-native narrative workflow
- Realism, horror, comedy, and general narrative controllers
- Mechanism and world-rule design references
- Scene graph and production adaptation methods
- Output templates
- Scoring and regression evals
- Static package validator

## Install for local Codex

Copy the top-level `ai-native-video-architect` folder into one of the skill locations recognized by your Codex environment.

Common current locations:

- User scope: `$HOME/.agents/skills/ai-native-video-architect`
- Repository scope: `<repo>/.agents/skills/ai-native-video-architect`

Restart Codex only if the new or changed skill is not detected automatically.

See `INSTALL.md` for Windows, macOS/Linux, and repository-scoped instructions.

## Invoke

Explicit:

```text
$ai-native-video-architect 帮我做一个90秒的现实主义AI原生短片，主题是持续在线带来的家庭压力。
```

Implicit examples:

```text
把这个传统短片剧本改成AI原生版本，但保留结尾。
```

```text
评价这个创意是不是只是在堆AI特效，不要重写。
```

```text
把这个方案拆成可生成镜头，给出稳定实现和失败备选。
```

## Validate

```bash
python scripts/validate_package.py
```

The script checks front matter, expected files, internal Markdown links, manifest coverage, and the single-`SKILL.md` constraint.

## Package notes

The skill is intentionally instruction-first. It does not depend on an MCP server or a specific video model. Model-specific adapters should be added as separate references and verified against current official model documentation.
