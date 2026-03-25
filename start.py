#!/usr/bin/env python3
"""
Content Machine - Interactive Pipeline
"""
import os
from pathlib import Path

def check_brand_config():
    """Step 1: Check if brand.md is filled"""
    brand_path = Path("config/brand.md")
    
    if not brand_path.exists():
        print("❌ config/brand.md n'existe pas.")
        print("   Crée-le d'abord avec ta config de marque.")
        return False
    
    content = brand_path.read_text()
    
    # Check if it's still template (has placeholders)
    if "[entrepreneurs non-tech" not in content and "## Audience cible" in content:
        lines = [l for l in content.split('\n') if l.strip() and not l.startswith('#')]
        if len(lines) < 10:
            print("⚠️  config/brand.md semble incomplet.")
            response = input("   Continuer quand même ? (o/n) : ")
            if response.lower() != 'o':
                return False
    
    print("✅ Brand config chargée")
    return True

def get_subject():
    """Step 2: Ask for subject"""
    print("\n" + "="*50)
    subject = input("📝 Sujet du post : ")
    if not subject.strip():
        print("❌ Sujet requis.")
        return None
    return subject.strip()

def get_type():
    """Step 3: Ask for type"""
    types = {
        "1": "story",
        "2": "tips", 
        "3": "contrarian",
        "4": "transformation",
        "5": "lesson",
        "6": "behind-the-scenes"
    }
    
    print("\n📋 Type de post :")
    print("   1. Story (engagement très élevé)")
    print("   2. Tips/Liste")
    print("   3. Contrarian (opinion tranchée)")
    print("   4. Transformation (avant/après)")
    print("   5. Lesson learned")
    print("   6. Behind-the-scenes")
    
    choice = input("\nChoix (1-6) [défaut: 1] : ").strip()
    
    if not choice:
        choice = "1"
    
    if choice not in types:
        print("❌ Choix invalide, défaut: story")
        return "story"
    
    print(f"✅ Type: {types[choice]}")
    return types[choice]

def get_notes():
    """Step 4: Ask for optional notes"""
    print("\n📌 Notes additionnelles (optionnel)")
    print("   (story à inclure, chiffres, contexte...)")
    print("   Appuie sur Entrée pour skip")
    
    notes = input("\nNotes : ").strip()
    
    if notes:
        print(f"✅ Notes enregistrées")
    else:
        print("   (pas de notes)")
    
    return notes

def load_context():
    """Load brand + rules"""
    brand = Path("config/brand.md").read_text()
    rules = Path("core/rules.md").read_text()
    return brand, rules

def load_engine_skills(engine: str, skill_type: str):
    """Load skill for an engine"""
    path = Path(f"engines/{engine}/{skill_type}/SKILL.md")
    if path.exists():
        return path.read_text()
    return ""

def display_output(subject, post_type, notes, brand, rules):
    """Display the generation prompt for both engines"""
    
    engine_a_hook = load_engine_skills("a-oneshot", "hook")
    engine_b_hook = load_engine_skills("b-iterative", "hook")
    
    print("\n" + "="*80)
    print("🚀 PIPELINE READY")
    print("="*80)
    
    print(f"\n📝 Sujet: {subject}")
    print(f"📋 Type: {post_type}")
    if notes:
        print(f"📌 Notes: {notes}")
    
    print("\n" + "-"*80)
    print("CONTEXT LOADED:")
    print("-"*80)
    print("✅ config/brand.md")
    print("✅ core/rules.md")
    
    print("\n" + "-"*80)
    print("ENGINES READY:")
    print("-"*80)
    print("✅ Engine A: engines/a-oneshot/ (curiosity-based, one-shot)")
    print("✅ Engine B: engines/b-iterative/ (outcome-first, 4 passes)")
    
    print("\n" + "="*80)
    print("📤 GÉNÈRE LES HOOKS")
    print("="*80)
    
    # Output the actual prompt to use
    print("""
Utilise ce contexte pour générer les hooks :

---
BRAND CONFIG:
""")
    print(brand[:500] + "..." if len(brand) > 500 else brand)
    
    print(f"""
---
SUJET: {subject}
TYPE: {post_type}
NOTES: {notes if notes else "(aucune)"}

---
Génère 5 hooks pour ENGINE A (curiosity/suspense) et 5 hooks pour ENGINE B (outcome-first/clarté).

Affiche côte à côte :

┌────────────────────────────────────────┬────────────────────────────────────────┐
│         ENGINE A (Curiosity)           │       ENGINE B (Outcome-First)         │
├────────────────────────────────────────┼────────────────────────────────────────┤
│ 1. [hook]                              │ 1. [hook]                              │
│ 2. [hook]                              │ 2. [hook]                              │
│ 3. [hook]                              │ 3. [hook]                              │
│ 4. [hook]                              │ 4. [hook]                              │
│ 5. [hook]                              │ 5. [hook]                              │
└────────────────────────────────────────┴────────────────────────────────────────┘

Puis demande : "Choisis 1 hook par engine (ex: A3, B1)"
""")

def main():
    print("\n" + "="*50)
    print("       CONTENT MACHINE - LinkedIn Pipeline")
    print("="*50)
    
    # Step 1: Check brand
    print("\n[1/4] Vérification config...")
    if not check_brand_config():
        return
    
    # Step 2: Get subject
    print("\n[2/4] Sujet")
    subject = get_subject()
    if not subject:
        return
    
    # Step 3: Get type
    print("\n[3/4] Type")
    post_type = get_type()
    
    # Step 4: Get notes
    print("\n[4/4] Notes")
    notes = get_notes()
    
    # Load context
    brand, rules = load_context()
    
    # Display output
    display_output(subject, post_type, notes, brand, rules)

if __name__ == "__main__":
    main()
