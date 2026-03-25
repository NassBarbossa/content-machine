# Content Machine

Self-improving content repurposing system with feedback loop.

## How it works

```
INPUT (topic) → GENERATE → OUTPUT → FEEDBACK → REFLECT → UPDATE RULES → LOOP
```

The system learns from your feedback and improves over time.

## Installation

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_key
```

## Usage

### Generate content

```bash
python cli.py generate "Mon sujet de contenu"

# Specific platforms
python cli.py generate "Mon sujet" --platforms linkedin x
```

### Give feedback

```bash
# Score 1-5
python cli.py feedback linkedin 4

# With comment
python cli.py feedback linkedin 2 --comment "Trop long, hook pas assez punchy"
```

### Add examples

```bash
# From file
python cli.py add-example linkedin --file my_best_post.txt --likes 150 --comments 30

# Interactive
python cli.py add-example linkedin
```

### View rules

```bash
python cli.py rules linkedin
```

## Architecture

```
content-machine/
├── cli.py                    # Terminal interface
├── core/
│   ├── orchestrator.py       # Main loop
│   ├── generator.py          # Content generation
│   ├── reflector.py          # Auto-critique & rule synthesis
│   └── memory.py             # Persistent storage
├── platforms/
│   ├── linkedin/
│   │   ├── examples.json     # Your best posts
│   │   └── rules.json        # Learned rules
│   ├── x/
│   └── instagram/
├── memory/
│   ├── feedback_buffer.json  # Recent feedbacks
│   └── history.json          # All events
└── config.yaml
```

## Self-improvement loop

1. **Generate** content using examples + rules
2. **Feedback** from user (1-5 score + comment)
3. **Reflect** on poor feedback (auto-critique)
4. **Synthesize** rules after 10 feedbacks
5. **Loop** with improved rules

## License

MIT
