# LinkedIn Post Generator

Génère le body d'un post LinkedIn à partir d'un hook validé.

## Avant de générer

### Questions à poser à l'user (si pas déjà répondu)

1. **Sujet/idée ?** — De quoi on parle ?
2. **Story ou expérience à référencer ?** — Du vécu à inclure ?
3. **Quel take / message à retenir ?** — La leçon principale ?
4. **Ton préféré ?** — casual | pro-casual | thought-leader
5. **CTA souhaité ?** — question | save | share | lien en commentaire

### Mémoire

Si `memory/voice.md` existe, le lire et appliquer le ton/style de l'user.

## Input

- **Hook** : Le hook choisi (généré par le hook skill)
- **Sujet** : Le sujet/angle du post
- **Type** : story | tips | contrarian | transformation | lesson-learned | behind-the-scenes

## Structure du post

```
[HOOK déjà fourni]

[BODY - 600-1000 caractères]

[CTA]

[2-3 hashtags]
```

## Voice Rules (OBLIGATOIRES)

### Écrire comme tu parles
- Lis à voix haute. Si ça sonne rigide, réécris.
- Première personne toujours.
- Contractions obligatoires ("j'ai", "c'est", "t'as", pas "j'ai fait", "cela est", "tu as")

### Spécifique > Générique
- ❌ "On a eu une grosse croissance"
- ✅ "On est passé de 12 à 47 clients en 3 mois"

### Mots interdits (buzzwords cringe)
- synergy, leverage, ecosystem, disrupt, game-changer
- "Je suis ravi d'annoncer...", "I'm humbled to..."
- "Dans le monde actuel en constante évolution..."
- "Voilà, j'espère que ça vous a plu..."
- Humble brags déguisés en leçons

## Règles de formatting (OBLIGATOIRES)

### Sauts de ligne
- **UNE phrase par ligne** (non négociable)
- **Ligne vide** entre chaque bloc/paragraphe
- Jamais plus de 2 phrases consécutives sans saut
- 1-2 phrases max par paragraphe

### Emphase
- CAPS pour les mots clés (pas de bold/italic)
- Pas plus de 2-3 mots en CAPS par post

### Longueur
- **Optimal : moins de 1300 caractères** (sauf story)
- Body : 600-1000 caractères
- Paragraphes : 1-2 phrases max

### Emojis & Hashtags
- **1 emoji max** dans tout le post (si vraiment nécessaire)
- Pas d'emojis comme bullet points
- 2-3 hashtags MAX, à la toute fin
- Jamais de hashtag dans le body

## Types de body

### 1. Story (engagement très élevé)

```
[Hook]

[Contexte - 1-2 lignes situant la scène]

[Le problème/la tension]

[Le tournant]

[La résolution]

[La leçon - 1 phrase punch]

[CTA]
```

### 2. Tips/Liste (engagement élevé)

```
[Hook]

[Intro courte - pourquoi ces tips]

1. [Tip 1]
[Explication courte]

2. [Tip 2]
[Explication courte]

3. [Tip 3]
[Explication courte]

[Récap ou leçon globale]

[CTA]
```

### 3. Contrarian (engagement élevé)

```
[Hook contrarian]

[Ce que tout le monde croit]

[Pourquoi c'est faux - avec data/exemple]

[Ce qui marche vraiment]

[Preuve/résultat]

[CTA provocant]
```

### 4. Transformation (engagement très élevé)

```
[Hook avant/après]

AVANT :
- [Point 1]
- [Point 2]
- [Point 3]

AUJOURD'HUI :
- [Point 1]
- [Point 2]
- [Point 3]

Ce qui a changé ?

[La révélation - 2-3 lignes]

[La leçon actionable]

[CTA]
```

### 5. Lesson Learned (engagement élevé)

```
[Hook "Je pensais X, puis Y, maintenant Z"]

[Ce que je croyais avant - et pourquoi]

[L'événement qui a tout changé]

[Ma nouvelle vision]

[Ce que ça a changé concrètement]

[CTA]
```

### 6. Behind-the-Scenes (engagement élevé)

```
[Hook "Voici comment X s'est vraiment passé"]

[Le contexte - ce que les gens voient de l'extérieur]

[La réalité - ce qui s'est vraiment passé]

[Les galères/surprises]

[Ce que j'en retiens]

[CTA]
```

## Formules CTA

| Type | Quand | Exemple |
|------|-------|---------|
| Question ouverte | Par défaut | "Et toi, c'est quoi ton plus gros blocage ?" |
| Expérience | Stories | "Ça t'est déjà arrivé ?" |
| Débat | Contrarian | "D'accord ou pas d'accord ?" |
| Ajout | Listes | "Tu ajouterais quoi ?" |
| Save | Tips actionnables | "Save pour plus tard" |
| Partage | Contenu inspirant | "Partage si ça résonne" |

## Ce qui tue un post

- ❌ Mur de texte sans sauts de ligne
- ❌ Paragraphes de 3+ phrases
- ❌ Jargon corporate (leverage, synergies, ecosystem)
- ❌ Conclusion molle ("Voilà, j'espère que...")
- ❌ Lien dans le body (mettre en commentaire)
- ❌ Plus de 3 hashtags
- ❌ Hashtags au milieu du texte
- ❌ Tirets longs "—"
- ❌ Plus d'1 emoji
- ❌ Humble brag déguisé en leçon
- ❌ Générique sans chiffres ni détails spécifiques

## Quality Check (avant de livrer)

- [ ] Hook ferait stop-scroll ?
- [ ] Sonne comme une personne, pas une marque ?
- [ ] White space (paragraphes courts + sauts de ligne) ?
- [ ] Au moins un détail spécifique (chiffre, nom, date) ?
- [ ] Finit avec engagement driver (question/CTA) ?
- [ ] Pas de buzzwords cringe ?
- [ ] Moins de 1300 caractères (sauf story) ?

## Exemple complet

**Input :**
- Hook : "J'ai fait 1 947€ en une heure."
- Sujet : VibeCoding
- Type : story

**Output :**

```
J'ai fait 1 947€ en une heure.

Sans produit.
Sans audience.
Sans publicité.

Juste une compétence que j'ai apprise en 30 jours.

Le VibeCoding.

C'est la capacité de créer des apps en décrivant ce que tu veux à une IA.

Pas besoin de savoir coder.

Voici comment j'ai fait :

1. J'ai identifié un problème
2. J'ai décrit la solution à Claude
3. En 47 min j'avais un outil fonctionnel
4. J'ai vendu l'accès à 97€

20 ventes le premier jour.

Le plus fou ?

Je sais toujours pas coder.

Tu veux apprendre à faire pareil ?

#VibeCoding #NoCode
```

## Output

Génère le post complet, prêt à copier-coller sur LinkedIn.
