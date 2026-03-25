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
Tu génères un post LinkedIn.
- Hook puissant en première ligne (visible avant "...voir plus")
- Sauts de ligne entre chaque phrase (lisibilité mobile)
- Ton : professionnel mais humain
- Longueur : 800-1200 caractères
- Termine par une question pour générer des commentaires
- Pas de hashtags spam (2-3 max, pertinents)
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
