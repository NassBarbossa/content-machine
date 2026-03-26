# AGENTS.md

Content Machine — génération de contenu LinkedIn avec A/B testing entre 2 engines.

## Init

À la première interaction ou quand l'user veut générer du contenu :

1. Lire `config/brand.md` — si vide ou incomplet, demander à l'user de le remplir d'abord
2. Lire `core/rules.md` — règles partagées

## Pipeline

**Étape 1 — Questions (AVANT de générer)**

Poser ces questions une par une :

1. "C'est quoi le sujet de ton post ?"
2. "Quel type ? (story | tips | contrarian | transformation | lesson | behind-the-scenes)"
3. "Raconte-moi la scène exacte : qu'est-ce qui s'est passé, où, quand, avec qui ? (le détail concret qui rend l'histoire vraie)"
4. "C'est quoi le moment clé / le déclic ? (la phrase, le geste, la réalisation)"
5. "T'as un chiffre, une preuve, un truc spécifique à inclure ?"
6. "Des notes ou contexte à ajouter ? (optionnel, Entrée pour skip)"

**IMPORTANT** : Si les réponses sont vagues ou manquent de détails concrets, relancer avec des questions de suivi AVANT de générer. Les engines produisent du générique quand elles n'ont pas assez de matière. Mieux vaut poser 2 questions de plus que générer un post moyen.

Attendre les réponses avant de continuer.

**Étape 2 — Générer les hooks**

Lire :
- `config/brand.md`
- `core/rules.md`  
- `engines/a-oneshot/hook/SKILL.md`
- `engines/b-iterative/hook/SKILL.md`

Générer 5 hooks par engine. Afficher côte à côte :

```
┌─────────────────────────────────────────┬─────────────────────────────────────────┐
│        ENGINE A (Curiosity)             │      ENGINE B (Outcome-First)           │
├─────────────────────────────────────────┼─────────────────────────────────────────┤
│ 1. [hook]                               │ 1. [hook]                               │
│ 2. [hook]                               │ 2. [hook]                               │
│ 3. [hook]                               │ 3. [hook]                               │
│ 4. [hook]                               │ 4. [hook]                               │
│ 5. [hook]                               │ 5. [hook]                               │
└─────────────────────────────────────────┴─────────────────────────────────────────┘
```

Demander : "Choisis 1 hook par engine (ex: A3, B1)"

**Étape 3 — Générer les posts**

Lire :
- `engines/a-oneshot/post/SKILL.md`
- `engines/b-iterative/post/SKILL.md`

Générer les posts avec les hooks choisis. Afficher côte à côte :

```
┌─────────────────────────────────────────┬─────────────────────────────────────────┐
│           POST A (one-shot)             │         POST B (4 passes)               │
├─────────────────────────────────────────┼─────────────────────────────────────────┤
│ [post complet]                          │ [post complet]                          │
│                                         │                                         │
│ (XXX caractères)                        │ (XXX caractères)                        │
└─────────────────────────────────────────┴─────────────────────────────────────────┘
```

Demander : "Lequel tu publies ? (A ou B)"

**Étape 4 — Logger le choix**

Stocker dans `memory/ab-test.json` :
- date
- sujet
- engine choisi (A ou B)
- raison (si donnée)

## Structure

```
content-machine/
├── config/brand.md           ← Config user (audience, ton, style)
├── core/rules.md             ← Règles partagées
├── engines/
│   ├── a-oneshot/            ← Curiosity hooks, one-shot post
│   │   ├── hook/SKILL.md
│   │   └── post/SKILL.md
│   └── b-iterative/          ← Outcome-first hooks, 4 passes
│       ├── hook/SKILL.md
│       └── post/SKILL.md
├── platforms/linkedin/skills/image/SKILL.md
└── memory/ab-test.json       ← Tracking A/B
```

## Règles

- Toujours charger `config/brand.md` + `core/rules.md` avant génération
- Output côte à côte pour comparer les engines
- Ne pas modifier `config/brand.md` sans demander
- Logger chaque choix A/B dans `memory/ab-test.json`

## Engines

| Engine | Philosophie | Process |
|--------|-------------|---------|
| A (one-shot) | Curiosity, suspense | Génération directe |
| B (iterative) | Outcome-first, clarté | 4 passes avec self-critique |
