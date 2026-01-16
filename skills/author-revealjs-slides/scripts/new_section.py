#!/usr/bin/env python3
import argparse
import html
import sys


def build_section(title: str, subtitle: str) -> list[str]:
    lines = []
    lines.append('<section class="layout-section">')
    lines.append(f"  <h2>{html.escape(title)}</h2>")
    if subtitle:
        lines.append(f'  <p class="subtitle">{html.escape(subtitle)}</p>')
    lines.append("</section>")
    return lines


def build_placeholder(title: str, index: int) -> list[str]:
    heading = f"{title} {index}"
    lines = []
    lines.append("<section>")
    lines.append(f"  <h2>{html.escape(heading)}</h2>")
    lines.append("  <ul>")
    lines.append("    <li>Key point</li>")
    lines.append("    <li>Evidence or example</li>")
    lines.append("    <li>Takeaway</li>")
    lines.append("  </ul>")
    lines.append("</section>")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a section divider + placeholder slides for Reveal.js."
    )
    parser.add_argument("title", help="Section title")
    parser.add_argument("--subtitle", default="", help="Optional subtitle")
    parser.add_argument(
        "--count",
        type=int,
        default=3,
        help="Number of placeholder slides to generate after the divider",
    )
    args = parser.parse_args()

    if args.count < 0:
        print("count must be 0 or greater", file=sys.stderr)
        return 1

    output = []
    output.extend(build_section(args.title, args.subtitle))
    for i in range(1, args.count + 1):
        output.append("")
        output.extend(build_placeholder(args.title, i))

    sys.stdout.write("\n".join(output) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
