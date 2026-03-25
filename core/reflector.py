"""
Reflector - Auto-critique and rule synthesis
"""
import os
from anthropic import Anthropic

def reflect_on_feedback(platform: str, feedback: dict, rules: list) -> dict:
    """
    After poor feedback, reflect on what went wrong and suggest new rules
    """
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    prompt = f"""# CONTEXT
J'ai généré du contenu {platform.upper()} qui a reçu un mauvais feedback.

Score : {feedback['score']}/5
Commentaire : {feedback.get('comment', 'Aucun')}

Règles actuelles :
{chr(10).join(f'- {r}' for r in rules) if rules else 'Aucune règle définie'}

# TASK
Analyse ce feedback et réponds en JSON :
{{
    "probleme": "Ce qui n'a probablement pas marché",
    "nouvelle_regle": "Une règle claire et actionnable à ajouter",
    "confiance": 0.8  // 0-1, ta confiance dans cette analyse
}}

Sois concis et actionnable.
"""
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}]
    )
    
    # Parse JSON response
    import json
    try:
        return json.loads(response.content[0].text)
    except:
        return {
            "probleme": "Analyse échouée",
            "nouvelle_regle": None,
            "confiance": 0
        }

def synthesize_rules(platform: str, feedbacks: list, reflections: list, current_rules: list) -> list:
    """
    After N feedbacks, synthesize all learnings into updated rules
    """
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    prompt = f"""# CONTEXT
J'ai accumulé des feedbacks et réflexions pour {platform.upper()}.

## Feedbacks récents
{chr(10).join(f"- Score {f['score']}/5: {f.get('comment', '')}" for f in feedbacks[-10:])}

## Réflexions
{chr(10).join(f"- {r.get('nouvelle_regle', '')}" for r in reflections if r.get('nouvelle_regle'))}

## Règles actuelles
{chr(10).join(f'- {r}' for r in current_rules) if current_rules else 'Aucune'}

# TASK
Synthétise tout ça en une liste de règles mises à jour (max 10 règles).
Fusionne les règles similaires, supprime les obsolètes, garde les essentielles.

Réponds en JSON :
{{
    "rules": ["règle 1", "règle 2", ...]
}}
"""
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}]
    )
    
    import json
    try:
        result = json.loads(response.content[0].text)
        return result.get("rules", current_rules)
    except:
        return current_rules
