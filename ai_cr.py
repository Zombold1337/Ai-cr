import requests
import subprocess
import sys

PROMPT_FILE = "prompts/review_ai_diff.txt"
MODEL = "qwen2.5-coder:7b"

def load_prompt():
    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        return f.read()

def get_git_diff():
    result = subprocess.run(
        ["git", "diff"],
        capture_output=True, text=True, encoding="utf-8"
    )
    return result.stdout

def ask_ollama(prompt_text):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": MODEL, "prompt": prompt_text, "stream": False}
    )
    return response.json()["response"]

def clean_yaml(text):
    text = text.strip()
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("yaml"):
            text = text[4:]
    return text.strip()

if __name__ == "__main__":
    diff_content = get_git_diff()

    if not diff_content.strip():
        print("Kein Diff gefunden. Hast du ungespeicherte Änderungen im Repo?")
        sys.exit(0)

    prompt_template = load_prompt()
    full_prompt = prompt_template.replace("{{DIFF_PLACEHOLDER}}", diff_content)

    print("Sende an Ollama, bitte warten...")
    result = ask_ollama(full_prompt)
    print(clean_yaml(result))