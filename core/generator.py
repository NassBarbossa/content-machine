"""
Generator - Generates content for each platform
"""
import os
from anthropic import Anthropic

def generate_content(topic: str, platform: str, examples: list, rules: list) -> str:
    """
    Generate content for a specific platform using LLM
    """
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    # Build prompt with examples and rules
    prompt = build_prompt(topic, platform, examples, rules)
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.content[0].text

def build_prompt(topic: str, platform: str, examples: list, rules: list) -> str:
    """
    Build the generation prompt with context
    """
    platform_instructions = {
        "linkedin": """
Tu génères un post LinkedIn à haute engagement.

STRUCTURE :
1. HOOK (première ligne) - Visible avant "...voir plus" (~210 car max). Doit captiver immédiatement.
2. BODY - Une phrase par ligne. Lignes vides entre paragraphes. Storytelling > listes.
3. CTA - Question ou demande d'engagement à la fin.
4. HASHTAGS - 2-3 max, pertinents, à la fin.

FORMULES DE HOOK QUI MARCHENT :
- Opinion contrarian : "Opinion impopulaire : [take]"
- Story : "J'ai [événement marquant]. [Résultat surprenant]."
- Stat : "[Chiffre surprenant]. Mais pas pour la raison que tu crois."
- Liste : "J'ai [action] [nombre]. Voici [X] leçons."
- Avant/après : "Il y a X ans : [situation]. Aujourd'hui : [transformation]."

RÈGLES DE FORMATTING :
- UNE phrase par ligne (obligatoire)
- Ligne vide entre chaque paragraphe
- Mots en CAPS pour emphase (pas de bold)
- Chiffres précis (1 947€, pas "presque 2000€")
- Pas de tirets longs "—"
- Pas de jargon corporate

ÉVITER :
- Murs de texte
- "Ravi d'annoncer...", "Dans le paysage actuel..."
- Commencer par hashtag ou emoji
- Liens dans le post (mets en commentaire)
- Plus de 3 hashtags

LONGUEUR : 800-1500 caractères optimal
""",
        "x": """
Tu génères un thread X/Twitter.
- Premier tweet = hook qui se suffit à lui-même
- 5-7 tweets max
- Chaque tweet doit fonctionner seul (les gens voient dans leur feed)
- Ton : punchy, direct
- Dernier tweet = CTA ou récap
- Pas de numérotation "1/", c'est daté
""",
        "instagram": """
Tu génères une caption Instagram.
- Hook en première ligne
- Corps du texte storytelling
- Emojis ok (pas spam)
- CTA pour engagement (save, share, comment)
- Hashtags à la fin (5-10, niche)
"""
    }
    
    prompt = f"""# TASK
Génère du contenu {platform.upper()} sur le sujet suivant :

SUJET : {topic}

# INSTRUCTIONS PLATEFORME
{platform_instructions.get(platform, "")}

"""
    
    if rules:
        prompt += "# RÈGLES APPRISES (à respecter absolument)\n"
        for rule in rules:
            prompt += f"- {rule}\n"
        prompt += "\n"
    
    if examples:
        prompt += "# EXEMPLES DE POSTS QUI MARCHENT\n"
        for i, ex in enumerate(examples[:3], 1):
            prompt += f"### Exemple {i}\n{ex['content']}\n\n"
    
    prompt += "# OUTPUT\nGénère le contenu maintenant. Pas d'explication, juste le post prêt à publier."
    
    return prompt
