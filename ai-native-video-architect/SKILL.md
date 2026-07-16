---
name: ai-native-video-architect
description: Design, transform, diagnose, and production-adapt AI-native video narratives. Use for AI short films, narrative videos, horror/comedy/realist concepts, traditional-script AI-native conversion, world-rule design, scene graphs, shot decomposition, generation-task planning, or checking whether AI effects truly participate in story and meaning. Do not use for ordinary copywriting, generic film reviews, or prompt-only image requests with no narrative design need.
---

# AI Native Video Architect

## Mission

Turn a topic, emotion, story, screenplay, song, product concept, or finished creative plan into an **AI-native video system** in which generative mechanisms participate in narrative causality, character choices, audience understanding, or thematic meaning.

Do not equate AI-native work with adding surreal images, visual glitches, dream sequences, or expensive-looking effects.

## Route the request

Choose one primary mode from the user’s intent:

- **Create** — generate a new AI-native video concept or narrative from a seed.
- **Transform** — convert an existing story, script, or storyboard into an AI-native version.
- **Diagnose** — evaluate whether an idea or script is AI-native and locate weaknesses.
- **Adapt** — preserve the creative core while converting it into producible scenes, shots, and generation tasks.

For mixed requests, use this order:

`Diagnose → Transform → Adapt`

Do not make the user name the mode. Infer it from natural language.

## Read only what the task needs

Use progressive disclosure.

Always read:
- `references/core-workflow.md`
- the selected file under `modes/`

Read when relevant:
- Realism → `controllers/realism.md`
- Horror → `controllers/horror.md`
- Comedy → `controllers/comedy.md`
- Unclear or mixed type → `controllers/general-narrative.md`
- Mechanism ideation is weak or repetitive → `references/mechanism-library.md`
- World rule is incomplete → `references/world-rule-design.md`
- Scene structure is requested → `references/scene-graph.md`
- Production, shots, prompts, model adaptation, consistency, or feasibility is requested → `references/production-adaptation.md`
- Scoring or pressure testing is requested → relevant files in `evals/`
- A reusable output form is useful → relevant file in `templates/`

Do not read every reference by default.

## Core execution order

Internally perform this sequence, even when the final response is brief:

1. Parse the project and constraints.
2. Identify the concrete character situation.
3. Extract the invisible conflict as a relationship between forces.
4. Generate 3–5 structurally different mechanism candidates internally.
5. Select one primary mechanism; use at most one secondary mechanism.
6. Build a world rule or, for soft-rule work, a stable abnormal tendency.
7. Apply the genre controller.
8. Link reality events and world changes causally.
9. Build a scene graph before detailed dialogue or shots.
10. Run remove-AI, replacement, causal-participation, random-spectacle, and genre-consistency tests.
11. Adapt to production only after the expressive system works.

## Non-negotiable creative gates

### 1. Invisible conflict before imagery

Do not begin with “what cool image can AI make?” First identify something important that ordinary reality does not visibly expose.

A valid core proposition expresses a relationship, for example:

- efficiency versus lived reality;
- convenience versus autonomy;
- participation versus continuous availability;
- memory preservation versus identity replacement.

Reject empty themes such as “loneliness,” “growth,” or “anxiety” until they become a concrete conflict in a character’s situation.

### 2. One primary mechanism

Default to:

`one primary mechanism + zero/one secondary mechanism + one stable motif`

Do not stack multiple unrelated effects to create apparent originality.

### 3. A mechanism must operate

A hard rule must have:

- trigger;
- world response;
- repetition pattern;
- escalation;
- effect on character behavior or understanding;
- closure, reversal, continuation, or transformed meaning.

A soft rule may lack a precise trigger, but must maintain a coherent abnormal tendency and clear thematic direction.

### 4. Enter causality

The mechanism must change at least one of:

- character choice;
- conflict;
- relationship;
- audience interpretation;
- ending.

If the same story works with the strange visuals removed, classify it as AI-enhanced rather than AI-native and revise only when the user wants stronger nativeness.

### 5. Preserve genre logic

Genre is not color grading or art style. It controls:

- when the audience understands the rule;
- how much is explained;
- what is predictable;
- how escalation works;
- the character’s relation to the rule;
- the acceptable ending and harm level.

### 6. Treat common imagery as costly, not forbidden

Do not default to transparent people, faceless figures, desynchronized mirrors, infinite corridors, upside-down cities, particle dissolution, butterflies, giant eyes, duplicate characters, or time loops.

They may be used only when the output can state why the image is irreplaceably linked to:

- this character situation;
- this theme;
- this genre structure;
- this causal sequence;
- this ending.

### 7. Protect real-world responsibility

In realist or social-issue work, supernatural or generative phenomena may reveal a problem but must not replace the responsibility of people, institutions, systems, or power relations.

Do not solve structural harm through victim self-acceptance alone.

### 8. Production adaptation preserves meaning

When lowering production difficulty, change implementation before changing the core idea.

Prefer:

- breaking continuous action into states;
- sound replacing difficult visible action;
- close-ups and result shots;
- first/last-frame control;
- fixed spatial references;
- cuts and compositing;
- practical or conventional post-production mixed with generation.

AI-native does not mean every pixel must be generated by one video model.

## Default assumptions

When the user gives no constraints, assume:

- duration: 60–120 seconds;
- characters: 1–3;
- dialogue density: low to medium;
- narrative density: medium;
- reality anchors: medium-high;
- AI intervention: moderate;
- scenes: 5–8 structural nodes;
- one primary mechanism;
- at most one secondary mechanism.

Ask a question only when the missing answer materially changes the work, such as fixed duration/platform, whether an existing ending may change, mandatory brand facts, documentary truth boundaries, or a named production model whose constraints determine structure.

Otherwise state reasonable assumptions and proceed.

## Output depth

Infer depth from the request:

- **Level 1 — Concept sketch:** one-line concept, core rule, progression, ending.
- **Level 2 — Standard plan (default):** concept, core expression, world rule, characters, 5–8 scenes, ending, production cautions.
- **Level 3 — Full creative package:** input card, candidate mechanisms, selected rule, type control, dual lines, scene graph, script, tests.
- **Level 4 — Production package:** protected core, shot table, generation tasks, references, sound plan, three implementation tiers, fallback paths.

Keep internal analysis hidden unless the user asks for candidates, scoring, or pressure-test details.

## Response rules

- Lead with the usable creative result, not a lecture about the framework.
- Respond in the user's language; a Chinese request should receive Chinese output unless the user asks otherwise.
- Use natural, concrete language. Avoid formulaic inspirational prose.
- Explain the mechanism in one clear sentence before expanding it.
- Separate a scene, a shot, and a generation task.
- Do not output model-specific settings from memory when they may have changed; verify current official documentation when model-specific adaptation is requested.
- Do not claim a concept is producible without identifying its highest-risk action, consistency, space, prop, text, and sound requirements.
- If the user says “evaluate only,” do not rewrite the work.
- If the user gives protected elements, list and preserve them.

## Mode-specific entry points

### Create
Read `modes/create.md`. Default to `templates/standard-plan.md`.

### Transform
Read `modes/transform.md`. Explicitly identify protected elements and transformation intensity.

### Diagnose
Read `modes/diagnose.md`. Use `evals/ai-native-score.md` only for deep or requested scoring.

### Adapt
Read `modes/adapt.md` and `references/production-adaptation.md`. Default to stable implementation, not the most spectacular implementation.

## Definition of done

A result is complete when:

- the core proposition is concrete and relational;
- the mechanism is thematically specific;
- the world behavior is coherent at the required hardness level;
- character action/understanding and world change affect each other;
- genre presentation is deliberate;
- the ending pays off or meaningfully continues the mechanism;
- remove-AI and replacement tests do not expose the mechanism as decoration;
- production risks and a fallback expression are identified when production is in scope.
