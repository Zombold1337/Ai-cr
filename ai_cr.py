import requests
import sys

PROMPT_FILE = "prompts/review_ai_diff.txt"
MODEL = "qwen2.5-coder:7b"

def load_prompt():
    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        return f.read()

def load_diff(diff_path):
    with open(diff_path, "r", encoding="utf-8") as f:
        return f.read()

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
    if len(sys.argv) < 2:
        print("Nutzung: python ai_cr.py <pfad-zum-diff>")
        sys.exit(1)

    diff_content = load_diff(sys.argv[1])
    prompt_template = load_prompt()
    full_prompt = prompt_template.replace("{{DIFF_PLACEHOLDER}}", diff_content)

    print("Sende an Ollama, bitte warten...")
    result = ask_ollama(full_prompt)
    print(clean_yaml(result))