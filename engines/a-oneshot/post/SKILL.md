# Engine A — Post Generator (One-Shot)

Génère le post complet en une passe.

## Input

- Hook validé
- Sujet
- Type : story | tips | contrarian | transformation | lesson | behind-the-scenes

## Process

**One-shot** : génère directement le post final.

## Types de body

### Story
```
[Hook]
[Contexte 1-2 lignes]
[Problème/tension]
[Tournant]
[Résolution]
[Leçon punch]
[CTA]
```

### Tips/Liste
```
[Hook]
[Intro courte]
1. [Tip + explication]
2. [Tip + explication]
3. [Tip + explication]
[Récap]
[CTA]
```

### Contrarian
```
[Hook]
[Ce que tout le monde croit]
[Pourquoi c'est faux + data]
[Ce qui marche vraiment]
[Preuve]
[CTA]
```

### Transformation
```
[Hook]
AVANT :
- [Point 1]
- [Point 2]
- [Point 3]

AUJOURD'HUI :
- [Point 1]
- [Point 2]
- [Point 3]

Ce qui a changé ?
[Révélation]
[CTA]
```

## CTA

Obligatoire. Question ouverte par défaut.

| Type | Exemple |
|------|---------|
| Question | "Et toi, c'est quoi ton blocage ?" |
| Expérience | "Ça t'est déjà arrivé ?" |
| Débat | "D'accord ou pas d'accord ?" |

## Output

Post complet avec character count.

## Quality Check

- [ ] Hook stop-scroll ?
- [ ] Sonne humain ?
- [ ] ≥1 preuve concrète ?
- [ ] 1,300-1,600 chars ?
- [ ] CTA présent ?
