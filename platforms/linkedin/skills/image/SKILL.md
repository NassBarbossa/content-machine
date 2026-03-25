# LinkedIn Image Generator

Specs et prompts pour les visuels LinkedIn.

## Specs par format

| Format | Dimensions | Usage |
|--------|------------|-------|
| Single image | 1200×627 (1.91:1) | Feed, link previews |
| Square | 1200×1200 | Single image |
| Vertical | 1080×1350 (4:5) | Mobile-first (88% users) |
| Carousel | 1080×1080 ou 1080×1350 | Multi-image (max 20) |
| Bannière | 1584×396 (4:1) | Profil |

- File : ≤10 MB, JPG/PNG
- Native uploads > liens externes
- Vertical préféré pour mobile

## Prompt templates

### Quote card
```
LinkedIn post image [DIMENSIONS].

Background: [couleur/gradient]
Style: [minimal/modern/bold]
Text: "[MESSAGE]"
Typography: clean sans-serif, bold

Professional, scroll-stopping. No stock photos.
```

### Bannière profil
```
LinkedIn banner 1584x396px.

Background: [couleur/gradient]
Accent colors: [couleurs]
Main text: "[HEADLINE]"
Subtext: "[TAGLINE]"

Style: [Modern/minimal/tech]. Clean, no clutter.
```

## Output

1. Dimensions exactes
2. Prompt pour génération IA
3. Guidelines design si création manuelle
