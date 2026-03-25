# LinkedIn Hook Generator

Génère des hooks qui font cliquer "voir plus".

## Contexte

Le hook = les ~210 premiers caractères visibles avant "...voir plus".

**Stats :**
- 7 secondes pour capter l'attention sur mobile
- Si le hook rate, 0% de lecture du reste
- Un bon hook = +300% de "voir plus" clicks

## Output

Génère **5 hooks** pour chaque sujet, un par formule.

## Formules

### 1. Opinion Contrarian
Prends le contre-pied de ce que tout le monde pense.

**Structure :** "Opinion impopulaire : [take controversé]"

**Exemples :**
- "Opinion impopulaire : les daily standups sont une perte de temps."
- "Opinion impopulaire : ton CV ne sert à rien."
- "Opinion impopulaire : le networking est surcoté."

**Psychologie :** Crée un pattern interrupt. Le cerveau veut savoir pourquoi tu penses différemment.

---

### 2. Story Personnelle
Commence par un événement marquant avec un résultat surprenant.

**Structure :** "[Événement marquant]. [Résultat inattendu]."

**Exemples :**
- "J'ai été viré un mardi. Meilleure chose qui me soit arrivée."
- "J'ai raté 47 entretiens. Le 48ème a changé ma vie."
- "J'ai perdu 50K€ en 3 mois. Voici ce que j'ai appris."

**Psychologie :** Curiosité gap. Comment un truc négatif peut donner un résultat positif ?

---

### 3. Stat Surprenante
Un chiffre qui choque + une promesse de révélation.

**Structure :** "[Stat choquante]. Mais pas pour la raison que tu crois."

**Exemples :**
- "92% des startups échouent. Mais pas pour la raison que tu crois."
- "J'ai analysé 500 posts LinkedIn. 3% génèrent 80% de l'engagement."
- "Les top performers travaillent 35h/semaine. Voici leur secret."

**Psychologie :** Le chiffre crée de la crédibilité. La suite crée de la curiosité.

---

### 4. Promesse de Liste
Tu as fait/vu quelque chose, tu en tires des leçons numérotées.

**Structure :** "J'ai [action] [nombre]. Voici [X] [leçons/erreurs/secrets]."

**Exemples :**
- "J'ai recruté 200+ devs. Voici 5 red flags que je cherche."
- "J'ai lancé 12 side projects. 11 ont échoué. Voici pourquoi."
- "J'ai lu 100 livres business cette année. 5 ont changé ma vie."

**Psychologie :** Le nombre donne de l'autorité. La liste promet de la valeur scannable.

---

### 5. Avant/Après
Transformation avec timeline + contraste fort.

**Structure :** "Il y a [temps] : [situation merdique]. Aujourd'hui : [situation désirable]."

**Exemples :**
- "Il y a 2 ans : 0 followers, 0 clients. Aujourd'hui : 15K followers, 12K€/mois."
- "Il y a 6 mois je ne savais pas coder. Aujourd'hui je facture 500€/jour."
- "2023 : burnout, dette, dépression. 2024 : 6 figures, temps libre, sérénité."

**Psychologie :** Le lecteur veut savoir comment faire la même transformation.

---

### 6. Statement Bold
Affirmation forte et directe qui interpelle.

**Structure :** "[Affirmation choc]. Voici pourquoi."

**Exemples :**
- "Ton diplôme ne vaut rien. Voici ce qui compte vraiment."
- "Arrête de chercher un mentor. Fais ça à la place."
- "Le meilleur investissement n'est pas la bourse."

**Psychologie :** Provoque une réaction émotionnelle immédiate (accord ou désaccord).

---

### 7. Pattern Interrupt
Casse le scroll avec une injonction directe.

**Structure :** "Stop. Avant de [action commune], [promesse]."

**Exemples :**
- "Stop. Avant d'envoyer ce cold email, lis ça."
- "Attends. Ne postule pas à ce job avant d'avoir vu ceci."
- "Pause. Ce que tu vas lire va changer ta façon de [domaine]."

**Psychologie :** Commande directe = le cerveau obéit automatiquement.

---

## Anti-patterns (ce qui tue un hook)

- ❌ "Ravi d'annoncer..." (corporate, ennuyeux)
- ❌ "Dans le paysage actuel..." (cliché vide)
- ❌ "Je voudrais partager..." (passif, lent)
- ❌ "Petit thread sur..." (dévalorisant)
- ❌ Commencer par emoji ou hashtag
- ❌ Question générique ("Tu veux réussir ?")
- ❌ Superlatifs vides ("incroyable", "révolutionnaire")

## Règles

1. **Max 210 caractères** (visible avant "voir plus")
2. **Chiffres précis** (1 947€, pas "presque 2K")
3. **Pas de tirets longs** "—"
4. **Première personne** quand possible (plus authentique)
5. **Tension ou curiosité** obligatoire

## Output Format

Pour chaque sujet, génère :

```
## Hooks pour : [SUJET]

**1. Contrarian**
[hook]

**2. Story**
[hook]

**3. Stat**
[hook]

**4. Liste**
[hook]

**5. Avant/Après**
[hook]
```
