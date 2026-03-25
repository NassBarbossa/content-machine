#!/usr/bin/env python3
"""
Content Machine CLI - A/B Testing LinkedIn Content
"""
import argparse
import sys
from core.orchestrator import Orchestrator

def print_side_by_side(title_a: str, content_a: list, title_b: str, content_b: list):
    """Affiche 2 colonnes côte à côte"""
    col_width = 40
    separator = "│"
    
    print("┌" + "─" * col_width + "┬" + "─" * col_width + "┐")
    print(f"│{title_a:^{col_width}}{separator}{title_b:^{col_width}}│")
    print("├" + "─" * col_width + "┼" + "─" * col_width + "┤")
    
    max_rows = max(len(content_a), len(content_b))
    for i in range(max_rows):
        a = content_a[i] if i < len(content_a) else ""
        b = content_b[i] if i < len(content_b) else ""
        
        # Truncate if too long
        a = a[:col_width-2] + ".." if len(a) > col_width else a
        b = b[:col_width-2] + ".." if len(b) > col_width else b
        
        print(f"│ {a:<{col_width-1}}{separator} {b:<{col_width-1}}│")
    
    print("└" + "─" * col_width + "┴" + "─" * col_width + "┘")

def main():
    parser = argparse.ArgumentParser(description="Content Machine - A/B Test LinkedIn Content")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Hooks command
    hooks_parser = subparsers.add_parser("hooks", help="Generate hooks from both engines")
    hooks_parser.add_argument("topic", help="Topic/subject for the post")
    
    # Post command
    post_parser = subparsers.add_parser("post", help="Generate posts from chosen hooks")
    post_parser.add_argument("topic", help="Topic/subject")
    post_parser.add_argument("--hook-a", required=True, help="Chosen hook for Engine A")
    post_parser.add_argument("--hook-b", required=True, help="Chosen hook for Engine B")
    post_parser.add_argument("--type", "-t", default="story", 
                            choices=["story", "tips", "contrarian", "transformation", "lesson", "behind-the-scenes"],
                            help="Post type")
    
    # Choice command (log A/B test result)
    choice_parser = subparsers.add_parser("choice", help="Log which post you chose")
    choice_parser.add_argument("topic", help="Topic of the post")
    choice_parser.add_argument("engine", choices=["A", "B", "a", "b"], help="Which engine won")
    choice_parser.add_argument("--reason", "-r", default="", help="Why you chose it")
    
    # Stats command
    stats_parser = subparsers.add_parser("stats", help="Show A/B test statistics")
    
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
        sys.exit(1)
    
    orchestrator = Orchestrator()
    
    if args.command == "hooks":
        print(f"\n🎯 Generating hooks for: {args.topic}\n")
        
        data = orchestrator.generate_hooks(args.topic)
        
        # Placeholder - in real use, this would call LLM
        print("=" * 85)
        print(f"{'ENGINE A (One-Shot / Curiosity)':^40} │ {'ENGINE B (Iterative / Outcome-First)':^40}")
        print("=" * 85)
        print()
        print("Load the skills and generate with your LLM:")
        print(f"  - Engine A: engines/a-oneshot/hook/SKILL.md")
        print(f"  - Engine B: engines/b-iterative/hook/SKILL.md")
        print(f"  - Context: config/brand.md + core/rules.md")
        print()
        print("Then run: python cli.py post <topic> --hook-a '<hook>' --hook-b '<hook>'")
    
    elif args.command == "post":
        print(f"\n📝 Generating posts for: {args.topic}\n")
        print(f"Hook A: {args.hook_a}")
        print(f"Hook B: {args.hook_b}")
        print(f"Type: {args.type}")
        print()
        print("Load the skills and generate with your LLM:")
        print(f"  - Engine A: engines/a-oneshot/post/SKILL.md")
        print(f"  - Engine B: engines/b-iterative/post/SKILL.md")
        print()
        print("After choosing, run: python cli.py choice <topic> A|B --reason '<why>'")
    
    elif args.command == "choice":
        summary = orchestrator.log_choice(args.topic, args.engine.upper(), args.reason)
        print(f"\n✅ Logged: Engine {args.engine.upper()} won for '{args.topic}'")
        print(f"\n📊 Current stats:")
        print(f"   Engine A wins: {summary['engine_a_wins']}")
        print(f"   Engine B wins: {summary['engine_b_wins']}")
    
    elif args.command == "stats":
        import json
        log_path = "memory/ab-test.json"
        try:
            with open(log_path, "r") as f:
                data = json.load(f)
            
            total = data["summary"]["engine_a_wins"] + data["summary"]["engine_b_wins"]
            
            print("\n📊 A/B Test Statistics\n")
            print(f"Total tests: {total}")
            print(f"Engine A wins: {data['summary']['engine_a_wins']}")
            print(f"Engine B wins: {data['summary']['engine_b_wins']}")
            
            if total > 0:
                pct_a = (data["summary"]["engine_a_wins"] / total) * 100
                pct_b = (data["summary"]["engine_b_wins"] / total) * 100
                print(f"\nEngine A: {pct_a:.1f}%")
                print(f"Engine B: {pct_b:.1f}%")
                
                if total >= 10:
                    winner = "A" if pct_a > pct_b else "B"
                    print(f"\n🏆 Recommendation: Engine {winner} is performing better")
            
        except FileNotFoundError:
            print("No tests logged yet.")

if __name__ == "__main__":
    main()
