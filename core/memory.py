"""
Memory - Manages examples, rules, feedbacks, and history
"""
import json
from pathlib import Path
from datetime import datetime

class Memory:
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.platforms_path = self.base_path / "platforms"
        self.memory_path = self.base_path / "memory"
    
    def _load_json(self, path: Path) -> dict | list:
        if path.exists():
            with open(path, "r") as f:
                return json.load(f)
        return [] if "examples" in str(path) or "rules" in str(path) else {}
    
    def _save_json(self, path: Path, data):
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    # Examples
    def get_examples(self, platform: str) -> list:
        path = self.platforms_path / platform / "examples.json"
        return self._load_json(path)
    
    def add_example(self, platform: str, content: str, metrics: dict = None):
        examples = self.get_examples(platform)
        examples.append({
            "content": content,
            "metrics": metrics or {},
            "added_at": datetime.now().isoformat()
        })
        path = self.platforms_path / platform / "examples.json"
        self._save_json(path, examples)
    
    # Rules
    def get_rules(self, platform: str) -> list:
        path = self.platforms_path / platform / "rules.json"
        return self._load_json(path)
    
    def update_rules(self, platform: str, rules: list):
        path = self.platforms_path / platform / "rules.json"
        self._save_json(path, rules)
    
    # Feedbacks
    def _get_feedback_buffer(self) -> dict:
        path = self.memory_path / "feedback_buffer.json"
        return self._load_json(path)
    
    def _save_feedback_buffer(self, buffer: dict):
        path = self.memory_path / "feedback_buffer.json"
        self._save_json(path, buffer)
    
    def add_feedback(self, platform: str, score: int, comment: str = ""):
        buffer = self._get_feedback_buffer()
        if platform not in buffer:
            buffer[platform] = {"feedbacks": [], "reflections": []}
        
        buffer[platform]["feedbacks"].append({
            "score": score,
            "comment": comment,
            "timestamp": datetime.now().isoformat()
        })
        self._save_feedback_buffer(buffer)
    
    def add_reflection(self, platform: str, reflection: dict):
        buffer = self._get_feedback_buffer()
        if platform not in buffer:
            buffer[platform] = {"feedbacks": [], "reflections": []}
        
        buffer[platform]["reflections"].append({
            **reflection,
            "timestamp": datetime.now().isoformat()
        })
        self._save_feedback_buffer(buffer)
    
    def feedback_count(self, platform: str) -> int:
        buffer = self._get_feedback_buffer()
        return len(buffer.get(platform, {}).get("feedbacks", []))
    
    def synthesize_rules(self, platform: str):
        """Synthesize feedbacks into new rules"""
        from .reflector import synthesize_rules
        
        buffer = self._get_feedback_buffer()
        platform_data = buffer.get(platform, {"feedbacks": [], "reflections": []})
        
        current_rules = self.get_rules(platform)
        new_rules = synthesize_rules(
            platform=platform,
            feedbacks=platform_data["feedbacks"],
            reflections=platform_data["reflections"],
            current_rules=current_rules
        )
        
        self.update_rules(platform, new_rules)
        
        # Clear buffer for this platform
        buffer[platform] = {"feedbacks": [], "reflections": []}
        self._save_feedback_buffer(buffer)
        
        # Log to history
        self._log_synthesis(platform, new_rules)
    
    def _log_synthesis(self, platform: str, rules: list):
        path = self.memory_path / "history.json"
        history = self._load_json(path) or []
        history.append({
            "event": "rules_synthesized",
            "platform": platform,
            "rules": rules,
            "timestamp": datetime.now().isoformat()
        })
        self._save_json(path, history)
