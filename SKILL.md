# Content Machine

Génération de contenu LinkedIn avec A/B testing entre 2 engines.

## Init

Avant de commencer :

1. **Vérifier `config/brand.md`** — doit être rempli avec :
   - Audience cible
   - Voice sliders (authority, warmth, etc.)
   - Positionnement
   - Mots autorisés/interdits
   - Exemples de style

2. **Charger `core/rules.md`** — règles partagées (formatting, banned words)

Si `config/brand.md` est vide ou template, demander à l'user de le remplir d'abord.

## Pipeline

```
1. CHECK CONFIG
   └── brand.md rempli ?
   
2. INPUT
   └── Demander : Sujet ?
   
3. TYPE
   └── Demander : Type ? (story | tips | contrarian | transformation | lesson | behind-the-scenes)
   
4. NOTES
   └── Demander : Notes additionnelles ? (optionnel)
   
5. GENERATE HOOKS (parallèle)
   ├── Engine A (curiosity) → 5 hooks
   └── Engine B (outcome-first) → 5 hooks
   
   Output côte à côte :
   ┌─────────────────────────────┬─────────────────────────────┐
   │     ENGINE A (Curiosity)    │   ENGINE B (Outcome-First)  │
   ├─────────────────────────────┼─────────────────────────────┤
   │ 1. [hook]                   │ 1. [hook]                   │
   │ 2. [hook]                   │ 2. [hook]                   │
   │ ...                         │ ...                         │
   └─────────────────────────────┴─────────────────────────────┘
   
   → Demander : "Choisis 1 hook par engine (ex: A3, B1)"

6. GENERATE POSTS (parallèle, avec hooks choisis)
   ├── Engine A (one-shot) → Post A
   └── Engine B (4 passes) → Post B
   
   Output côte à côte :
   ┌─────────────────────────────┬─────────────────────────────┐
   │        POST A               │        POST B               │
   │        (one-shot)           │        (4 passes)           │
   ├─────────────────────────────┼─────────────────────────────┤
   │ [post complet]              │ [post complet]              │
   │ [character count]           │ [character count]           │
   └─────────────────────────────┴─────────────────────────────┘
   
   → Demander : "Lequel tu publies ? (A ou B)"

7. LOG CHOICE
   └── Stocker dans memory/ab-test.json
```

## Fichiers

| Fichier | Rôle |
|---------|------|
| `config/brand.md` | Config user (audience, ton, style) |
| `core/rules.md` | Règles partagées |
| `engines/a-oneshot/hook/SKILL.md` | Hooks curiosity |
| `engines/a-oneshot/post/SKILL.md` | Post one-shot |
| `engines/b-iterative/hook/SKILL.md` | Hooks outcome-first |
| `engines/b-iterative/post/SKILL.md` | Post 4 passes |
| `memory/ab-test.json` | Tracking A/B |

## Engines

### Engine A — One-Shot (Curiosity)
- Hooks basés sur curiosité, suspense, pattern interrupt
- Post généré en une passe
- CTA obligatoire
- Cible : audience générale

### Engine B — Iterative (Outcome-First)
- Hooks basés sur résultat immédiat, clarté
- Post généré en 4 passes avec self-critique
- CTA soft et optionnel
- Cible : B2B/Exec
