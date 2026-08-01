import requests
import subprocess
import sys

PROMPT_FILE = "prompts/review_ai_diff.txt"
MODEL = "qwen2.5-coder:7b"
OLLAMA_URL = "http://localhost:11434/api/generate"

def load_prompt():
    try:
        with open(PROMPT_FILE, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Fehler: Prompt-Datei nicht gefunden unter '{PROMPT_FILE}'.")
        print("Stelle sicher, dass du das Skript im richtigen Ordner ausführst.")
        sys.exit(1)

def get_git_diff():
    try:
        result = subprocess.run(
            ["git", "diff", "--cached" ],
            capture_output=True, text=True, encoding="utf-8"
        )
    except FileNotFoundError:
        print("Fehler: Git wurde nicht gefunden. Ist Git installiert und im PATH?")
        sys.exit(1)

    if result.returncode != 0:
        print("Fehler: 'git diff' konnte nicht ausgeführt werden.")
        print("Bist du in einem gültigen Git-Repository?")
        print(result.stderr)
        sys.exit(1)

    return result.stdout

def ask_ollama(prompt_text):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL, "prompt": prompt_text, "stream": False},
            timeout=120
        )
    except requests.exceptions.ConnectionError:
        print("Fehler: Konnte keine Verbindung zu Ollama herstellen.")
        print("Läuft Ollama gerade? Starte die Ollama-App und versuch's erneut.")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print("Fehler: Ollama hat zu lange gebraucht (Timeout nach 120 Sekunden).")
        print("Ist das Modell geladen? Versuch: ollama run qwen2.5-coder:7b")
        sys.exit(1)

    if response.status_code != 200:
        print(f"Fehler: Ollama hat mit Status {response.status_code} geantwortet.")
        print(response.text)
        sys.exit(1)

    try:
        return response.json()["response"]
    except (KeyError, ValueError):
        print("Fehler: Unerwartete Antwort von Ollama erhalten.")
        sys.exit(1)

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