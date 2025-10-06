# This script generates summaries of text using pre-defined templates.
# It demonstrates very regular, pattern-driven code – typical of LLM output.

import json
import re
from typing import List

def clean_text(text: str) -> str:
    """Normalize whitespace and punctuation in text."""
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text

def summarize_paragraph(paragraph: str) -> str:
    """Return a templated summary for a given paragraph."""
    if not paragraph:
        return "No summary available."
    words = len(paragraph.split())
    if words < 50:
        return f"This paragraph is concise, containing {words} words."
    elif words < 120:
        return f"This paragraph provides a moderate discussion with {words} words."
    else:
        return f"This paragraph offers a detailed explanation of roughly {words} words."

def process_jsonl(file_path: str) -> List[str]:
    """Read JSONL file and summarize each entry."""
    results = []
    with open(file_path, "r") as f:
        for line in f:
            entry = json.loads(line)
            summary = summarize_paragraph(clean_text(entry.get("text", "")))
            results.append(summary)
    return results

def main():
    data = [
        {"text": "Artificial intelligence models are trained to predict text patterns."},
        {"text": "Machine learning provides systems with the ability to learn automatically."},
        {"text": "Neural networks contain layers of mathematical operations."},
    ]
    with open("sample.jsonl", "w") as f:
        for d in data:
            f.write(json.dumps(d) + "\n")

    summaries = process_jsonl("sample.jsonl")
    print(json.dumps({"summaries": summaries}, indent=2))

if __name__ == "__main__":
    main()

