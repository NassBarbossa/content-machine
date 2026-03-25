# LinkedIn Image Generator

Génère les specs et prompts pour les visuels LinkedIn.

## Quand utiliser

- Post avec image
- Carousel
- Bannière de profil
- Thumbnail pour articles

## Specs par format

### Post - Single Image
- **Dimensions** : 1200×627 (ratio 1.91:1)
- **Usage** : Feed standard, link previews
- **File** : ≤10 MB, JPG/PNG

### Post - Square
- **Dimensions** : 1200×1200 (ratio 1:1)
- **Usage** : Single image, meilleure visibilité mobile

### Post - Vertical (Recommandé)
- **Dimensions** : 1080×1350 (ratio 4:5)
- **Usage** : 88% des users sont sur mobile, vertical prend plus de place dans le feed

### Carousel
- **Dimensions** : 1080×1080 ou 1080×1350
- **Slides** : Jusqu'à 20 images
- **Format** : PDF ou images multiples
- **Usage** : Contenu éducatif, tips, storytelling visuel

### Bannière de profil
- **Dimensions** : 1584×396 (ratio 4:1)
- **Usage** : Branding personnel, value prop, CTA

## Règles générales

- **Native uploads > liens externes** (meilleur reach)
- **Vertical préféré** pour mobile
- **Texte lisible** : min 24px sur mobile
- **Pas de texte trop petit** dans la bannière
- **Contraste fort** pour lisibilité

## Prompt template pour génération IA

### Single image / Quote card

```
LinkedIn post image, [DIMENSIONS].

Design:
- Background: [couleur ou gradient]
- Style: [minimal/modern/corporate/bold]
- Text: "[QUOTE OU MESSAGE]"
- Typography: [clean sans-serif, bold]

Mood: Professional, engaging, scroll-stopping.
No stock photos, no faces unless specified.
```

### Bannière de profil

```
LinkedIn banner 1584x396px.

Design:
- Background: [couleur/gradient]
- Accent colors: [couleurs]
- Main text: "[HEADLINE OU VALUE PROP]"
- Subtext: "[TAGLINE]" (optional)

Style: [Modern/minimal/tech/corporate]. Clean, professional.
No cluttered elements, no small unreadable text.
```

### Carousel slide

```
LinkedIn carousel slide 1080x1350px (slide [X] of [Y]).

Content:
- Title: "[TITRE]"
- Body: "[CONTENU]"
- Visual: [icon/illustration si nécessaire]

Style: Consistent with brand colors [COULEURS].
Clear hierarchy, one idea per slide.
```

## Output

Pour chaque demande, fournir :
1. **Dimensions** exactes
2. **Prompt** pour génération IA (Gemini, Midjourney, DALL-E)
3. **Guidelines** de design si création manuelle
