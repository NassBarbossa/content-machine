"""
Orchestrator - Manages the content generation loop
"""
import json
from pathlib import Path
from .generator import generate_content
from .reflector import reflect_on_feedback
from .memory import Memory

class Orchestrator:
    def __init__(self, config_path: str = "config.yaml"):
        self.memory = Memory()
        self.platforms = ["linkedin", "x", "instagram"]
    
    def run(self, topic: str, platforms: list = None):
        """
        Main loop:
        1. Generate content for each platform
        2. Return outputs
        """
        if platforms is None:
            platforms = self.platforms
        
        outputs = {}
        for platform in platforms:
            outputs[platform] = generate_content(
                topic=topic,
                platform=platform,
                examples=self.memory.get_examples(platform),
                rules=self.memory.get_rules(platform)
            )
        
        return outputs
    
    def feedback(self, platform: str, score: int, comment: str = ""):
        """
        Process user feedback:
        1. Store feedback
        2. Auto-reflect if score < 4
        3. Synthesize rules if buffer full
        """
        self.memory.add_feedback(platform, score, comment)
        
        # Auto-reflect on poor scores
        if score < 4:
            reflection = reflect_on_feedback(
                platform=platform,
                feedback={"score": score, "comment": comment},
                rules=self.memory.get_rules(platform)
            )
            self.memory.add_reflection(platform, reflection)
        
        # Synthesize rules if buffer is full
        if self.memory.feedback_count(platform) >= 10:
            self.memory.synthesize_rules(platform)
    
    def add_example(self, platform: str, content: str, metrics: dict = None):
        """Add a high-performing example"""
        self.memory.add_example(platform, content, metrics)
