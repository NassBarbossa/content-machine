# LinkedIn Post Generator

Génère le body d'un post LinkedIn à partir d'un hook validé.

## Input

- **Hook** : Le hook choisi (généré par le hook skill)
- **Sujet** : Le sujet/angle du post
- **Type** : story | tips | contrarian | transformation (optionnel)

## Structure du post

```
[HOOK déjà fourni]

[BODY - 600-1200 caractères]

[CTA]

[2-3 hashtags]
```

## Règles de formatting (OBLIGATOIRES)

### Sauts de ligne
- **UNE phrase par ligne** (non négociable)
- **Ligne vide** entre chaque bloc/paragraphe
- Jamais plus de 2 phrases consécutives sans saut

### Emphase
- CAPS pour les mots clés (pas de bold/italic)
- Pas plus de 2-3 mots en CAPS par post

### Longueur
- Body : 600-1200 caractères
- Total post : 800-1500 caractères
- Paragraphes : 1-3 phrases max

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

## Formules CTA

| Type | Quand | Exemple |
|------|-------|---------|
| Question ouverte | Par défaut | "Et toi, c'est quoi ton plus gros blocage ?" |
| Expérience | Stories | "Ça t'est déjà arrivé ?" |
| Débat | Contrarian | "D'accord ou pas d'accord ?" |
| Ajout | Listes | "Tu ajouterais quoi ?" |
| Save | Tips actionnables | "Save pour plus tard 🔖" |
| Partage | Contenu inspirant | "Partage si ça résonne ♻️" |

## Ce qui tue un post

- ❌ Mur de texte sans sauts de ligne
- ❌ Paragraphes de 4+ phrases
- ❌ Jargon corporate ("leverage", "synergies")
- ❌ Conclusion molle ("Voilà, j'espère que...")
- ❌ Lien dans le body (mettre en commentaire)
- ❌ Plus de 3 hashtags
- ❌ Hashtags au milieu du texte
- ❌ Tirets longs "—"
- ❌ Trop d'emojis (max 2-3)

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

1. J'ai identifié un problème (les gens galèrent à créer des landing pages)
2. J'ai décrit la solution à Claude
3. En 47 min j'avais un outil fonctionnel
4. J'ai vendu l'accès à 97€

20 ventes le premier jour.

Le plus fou ?

Je ne sais toujours pas coder.

Tu veux apprendre à faire pareil ?

#VibeCoding #NoCode #Entrepreneuriat
```

## Output

Génère le post complet, prêt à copier-coller sur LinkedIn.
