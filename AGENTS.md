# AGENTS.md

Content Machine — génération de contenu LinkedIn avec A/B testing entre 2 engines.

## Init

Avant toute génération :

1. Lire `config/brand.md` — si vide ou incomplet, demander à l'user de le remplir
2. Lire `core/rules.md` — règles partagées (formatting, banned words)

## Pipeline

Quand l'user veut générer du contenu :

```
1. CHECK
   └── config/brand.md rempli ?

2. DEMANDER
   └── Sujet ?

3. DEMANDER
   └── Type ? (story | tips | contrarian | transformation | lesson | behind-the-scenes)

4. DEMANDER
   └── Notes ? (optionnel)

5. GÉNÉRER HOOKS (parallèle)
   ├── Lire engines/a-oneshot/hook/SKILL.md → 5 hooks
   └── Lire engines/b-iterative/hook/SKILL.md → 5 hooks
   
   Afficher côte à côte :
   ┌─────────────────────────────┬─────────────────────────────┐
   │     ENGINE A (Curiosity)    │   ENGINE B (Outcome-First)  │
   ├─────────────────────────────┼─────────────────────────────┤
   │ 1. [hook]                   │ 1. [hook]                   │
   │ 2. [hook]                   │ 2. [hook]                   │
   │ 3. [hook]                   │ 3. [hook]                   │
   │ 4. [hook]                   │ 4. [hook]                   │
   │ 5. [hook]                   │ 5. [hook]                   │
   └─────────────────────────────┴─────────────────────────────┘
   
   Demander : "Choisis 1 hook par engine (ex: A3, B1)"

6. GÉNÉRER POSTS (parallèle)
   ├── Lire engines/a-oneshot/post/SKILL.md → Post avec hook A
   └── Lire engines/b-iterative/post/SKILL.md → Post avec hook B
   
   Afficher côte à côte :
   ┌─────────────────────────────┬─────────────────────────────┐
   │         POST A              │         POST B              │
   ├─────────────────────────────┼─────────────────────────────┤
   │ [post]                      │ [post]                      │
   │ (XXX chars)                 │ (XXX chars)                 │
   └─────────────────────────────┴─────────────────────────────┘
   
   Demander : "Lequel tu publies ? (A ou B)"

7. LOG
   └── Stocker le choix dans memory/ab-test.json
```

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
