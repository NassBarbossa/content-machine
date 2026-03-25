"""
Orchestrator - Charge config, dispatch aux engines A et B en parallèle
"""
import os
from pathlib import Path

class Orchestrator:
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.config = self._load_config()
        self.rules = self._load_rules()
    
    def _load_file(self, path: Path) -> str:
        if path.exists():
            with open(path, "r") as f:
                return f.read()
        return ""
    
    def _load_config(self) -> str:
        return self._load_file(self.base_path / "config" / "brand.md")
    
    def _load_rules(self) -> str:
        return self._load_file(self.base_path / "core" / "rules.md")
    
    def get_context(self) -> dict:
        """Retourne le contexte à injecter dans chaque engine"""
        return {
            "brand": self.config,
            "rules": self.rules
        }
    
    def generate_hooks(self, topic: str) -> dict:
        """
        Génère les hooks via les 2 engines en parallèle
        Retourne les 2 sets de hooks pour comparaison
        """
        context = self.get_context()
        
        # Engine A - One-shot (curiosity-based)
        engine_a_skill = self._load_file(
            self.base_path / "engines" / "a-oneshot" / "hook" / "SKILL.md"
        )
        
        # Engine B - Iterative (outcome-first)
        engine_b_skill = self._load_file(
            self.base_path / "engines" / "b-iterative" / "hook" / "SKILL.md"
        )
        
        return {
            "topic": topic,
            "context": context,
            "engine_a": {
                "name": "One-Shot (Curiosity)",
                "skill": engine_a_skill
            },
            "engine_b": {
                "name": "Iterative (Outcome-First)",
                "skill": engine_b_skill
            }
        }
    
    def generate_posts(self, hook_a: str, hook_b: str, topic: str, post_type: str) -> dict:
        """
        Génère les posts via les 2 engines avec les hooks choisis
        """
        context = self.get_context()
        
        engine_a_skill = self._load_file(
            self.base_path / "engines" / "a-oneshot" / "post" / "SKILL.md"
        )
        
        engine_b_skill = self._load_file(
            self.base_path / "engines" / "b-iterative" / "post" / "SKILL.md"
        )
        
        return {
            "topic": topic,
            "type": post_type,
            "context": context,
            "engine_a": {
                "name": "One-Shot",
                "hook": hook_a,
                "skill": engine_a_skill
            },
            "engine_b": {
                "name": "Iterative (4 passes)",
                "hook": hook_b,
                "skill": engine_b_skill
            }
        }
    
    def log_choice(self, topic: str, chosen_engine: str, reason: str = ""):
        """Log le choix de l'user pour A/B testing"""
        import json
        from datetime import datetime
        
        log_path = self.base_path / "memory" / "ab-test.json"
        
        # Load existing
        if log_path.exists():
            with open(log_path, "r") as f:
                data = json.load(f)
        else:
            data = {"tests": [], "summary": {"engine_a_wins": 0, "engine_b_wins": 0}}
        
        # Add new test
        data["tests"].append({
            "date": datetime.now().isoformat(),
            "topic": topic,
            "chosen": chosen_engine,
            "reason": reason
        })
        
        # Update summary
        if chosen_engine.upper() == "A":
            data["summary"]["engine_a_wins"] += 1
        elif chosen_engine.upper() == "B":
            data["summary"]["engine_b_wins"] += 1
        
        # Save
        with open(log_path, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return data["summary"]
