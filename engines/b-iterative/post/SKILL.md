# Engine B — Post Generator (Iterative - 4 Passes)

Génère le post en 4 passes avec self-revision.

## Input

- Hook validé
- Sujet
- Type : milestone | product-ship | customer-story | metrics | learning | behind-the-scenes

## Process (4 passes)

### V1 — Draft

Génère le post brut :
- 1-2 ligne hook avec outcome + context
- Body : 3-5 phrases/bullets avec proof points
- 1 ligne "why it matters"
- Credits (optionnel) + soft CTA (optionnel)

---

### Self-critique A (mécanique)

Vérifie et corrige :
- [ ] Phrases vagues ? → remplacer par verbes concrets
- [ ] Preuves ≥2 ? (chiffres, dates, noms, before/after, artifact)
- [ ] Banned words ? → supprimer
- [ ] Phrases >22 mots ? → split
- [ ] 3 premières lignes fonctionnent seules ? (truncate test)

---

### V2 — Sharper

Applique les fixes de A :
- Renforcer hook avec chiffre ou contraste
- Remplacer 1 adjectif par une métrique
- Ajouter 1 artifact stub ("case study en commentaire")
- Garder warmth, pas de cheerleading

---

### Self-critique B (reader/algo)

Vérifie :
- [ ] Un busy reader apprend 1 truc utile en 30 sec ?
- [ ] Proof density ≥2 ?
- [ ] Paragraphes ≤3 lignes ?
- [ ] Hook améliore dwell time ? Si non, rewrite.

---

### V3 — Final

Post publication-ready :
- Humain, confiant, factuel
- Prêt à coller dans LinkedIn
- 2-3 hashtags fonctionnels (seulement si utiles)

## CTA

**Soft et optionnel.** Seulement si genuinely helpful.

| Type | Exemple |
|------|---------|
| Artifact | "Pilot notes en commentaire" |
| DM | "DM pour le teardown" |
| Hiring | "On recrute : 2 postes backend" |

## Output

Afficher V1, V2, V3 avec character count pour chaque.

Ou seulement V3 si user demande juste le final.

## Quality Check (intégré dans les passes)

- Proof density ≥2
- Paragraphes ≤3 lignes
- 120-180 mots (~800-1200 chars)
- 0-1 emoji
- 0-2 hashtags fonctionnels
