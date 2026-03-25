#!/usr/bin/env python3
"""
Content Machine CLI
"""
import argparse
import sys
from core import Orchestrator

def main():
    parser = argparse.ArgumentParser(description="Content Machine - Self-improving content repurposing")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Generate command
    gen_parser = subparsers.add_parser("generate", help="Generate content from a topic")
    gen_parser.add_argument("topic", help="The topic/subject to create content about")
    gen_parser.add_argument("--platforms", "-p", nargs="+", choices=["linkedin", "x", "instagram"],
                           default=["linkedin", "x"], help="Platforms to generate for")
    
    # Feedback command
    fb_parser = subparsers.add_parser("feedback", help="Give feedback on generated content")
    fb_parser.add_argument("platform", choices=["linkedin", "x", "instagram"])
    fb_parser.add_argument("score", type=int, choices=[1, 2, 3, 4, 5])
    fb_parser.add_argument("--comment", "-c", default="", help="Optional comment")
    
    # Add example command
    ex_parser = subparsers.add_parser("add-example", help="Add a high-performing example")
    ex_parser.add_argument("platform", choices=["linkedin", "x", "instagram"])
    ex_parser.add_argument("--file", "-f", help="File containing the example")
    ex_parser.add_argument("--likes", type=int, default=0)
    ex_parser.add_argument("--comments", type=int, default=0)
    
    # Show rules command
    rules_parser = subparsers.add_parser("rules", help="Show current rules for a platform")
    rules_parser.add_argument("platform", choices=["linkedin", "x", "instagram"])
    
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
        sys.exit(1)
    
    orchestrator = Orchestrator()
    
    if args.command == "generate":
        print(f"\n🚀 Generating content for: {args.topic}\n")
        print("=" * 50)
        
        outputs = orchestrator.run(args.topic, args.platforms)
        
        for platform, content in outputs.items():
            print(f"\n### {platform.upper()} ###\n")
            print(content)
            print("\n" + "-" * 50)
        
        print("\n💡 Use 'content-machine feedback <platform> <score>' to give feedback")
    
    elif args.command == "feedback":
        orchestrator.feedback(args.platform, args.score, args.comment)
        print(f"✅ Feedback recorded for {args.platform}: {args.score}/5")
        if args.score < 4:
            print("🔄 Auto-reflection triggered")
    
    elif args.command == "add-example":
        if args.file:
            with open(args.file, "r") as f:
                content = f.read()
        else:
            print("Paste your example (Ctrl+D when done):")
            content = sys.stdin.read()
        
        orchestrator.add_example(
            args.platform,
            content,
            {"likes": args.likes, "comments": args.comments}
        )
        print(f"✅ Example added for {args.platform}")
    
    elif args.command == "rules":
        rules = orchestrator.memory.get_rules(args.platform)
        if rules:
            print(f"\n📋 Rules for {args.platform.upper()}:\n")
            for i, rule in enumerate(rules, 1):
                print(f"  {i}. {rule}")
        else:
            print(f"No rules defined for {args.platform} yet.")

if __name__ == "__main__":
    main()
