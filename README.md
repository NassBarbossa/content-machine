# Content Machine

Self-improving content generation with A/B testing between 2 engines.

## Architecture

```
content-machine/
├── config/
│   └── brand.md              ← Your brand config (audience, tone, style)
├── core/
│   ├── rules.md              ← Shared rules (formatting, banned words)
│   └── orchestrator.py       ← Loads config, dispatches to engines
├── engines/
│   ├── a-oneshot/            ← Engine A: One-shot, curiosity-based hooks
│   │   ├── hook/SKILL.md
│   │   └── post/SKILL.md
│   └── b-iterative/          ← Engine B: 4-pass, outcome-first hooks
│       ├── hook/SKILL.md
│       └── post/SKILL.md
├── platforms/
│   └── linkedin/
│       └── skills/
│           └── image/SKILL.md
└── memory/
    └── ab-test.json          ← A/B test results
```

## Pipeline

```
1. CONFIG
   └── Load config/brand.md + core/rules.md

2. INPUT
   └── Topic + Type

3. ORCHESTRATOR
   └── Dispatch to Engine A + Engine B (parallel)

4. HOOKS (parallel)
   ┌─────────────────┐    ┌─────────────────┐
   │   ENGINE A      │    │   ENGINE B      │
   │   5 hooks       │    │   5 hooks       │
   │   (curiosity)   │    │   (outcome)     │
   └────────┬────────┘    └────────┬────────┘
            │                      │
            ▼                      ▼
        5 hooks A             5 hooks B
   
   User chooses 1 hook from A + 1 hook from B

5. POSTS (parallel, with chosen hooks)
   ┌─────────────────┐    ┌─────────────────┐
   │   ENGINE A      │    │   ENGINE B      │
   │   (one-shot)    │    │   (4 passes)    │
   └────────┬────────┘    └────────┬────────┘
            │                      │
            ▼                      ▼
        Post A                Post B

6. OUTPUT
   Side-by-side comparison
   User chooses which to publish

7. FEEDBACK
   Log choice → memory/ab-test.json
   After 1 week → stats → keep best engine
```

## Usage

### Generate hooks
```bash
python cli.py hooks "Mon sujet de contenu"
```

### Generate posts (after choosing hooks)
```bash
python cli.py post "Mon sujet" --hook-a "Hook choisi A" --hook-b "Hook choisi B" --type story
```

### Log your choice
```bash
python cli.py choice "Mon sujet" A --reason "Plus punchy"
```

### View stats
```bash
python cli.py stats
```

## Engines

### Engine A — One-Shot (Curiosity)
- Hooks based on curiosity gap, pattern interrupt
- Post generated in one pass
- CTA obligatory
- Target: General audience

### Engine B — Iterative (Outcome-First)  
- Hooks based on outcome first, clarity
- Post generated in 4 passes with self-critique
- Soft CTA (optional)
- Target: B2B/Exec audience

## Customization

Edit `config/brand.md` to set:
- Target audience
- Voice sliders (authority, warmth, humor, etc.)
- Positioning
- Allowed/banned words
- Style examples

## A/B Testing

After 1 week of testing, run `python cli.py stats` to see which engine performs better for your audience. Then you can:
1. Keep only the winning engine
2. Merge best practices from both
3. Continue testing with variations
