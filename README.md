# Ai-cr – AI Change Reviewer

Ein kleines, **lokales** Tool, das AI-generierten Code (von Cursor, Claude, Copilot, Aider, Windsurf usw.) prüft, **bevor** du commitest.

- Erkennt typische AI-Fehler (Halluzinationen, subtile Bugs, Over-Refactoring, Security-Probleme)
- Läuft komplett offline mit Ollama (keine Cloud, keine Kosten, kein Datenschutz-Risiko)
- Kann als Pre-Commit-Hook laufen
- Noch ganz am Anfang – erste Version kommt bald!

## Warum das nützlich ist
Viele Entwickler werden durch AI schneller, aber AI macht auch subtile Fehler, die man später debuggen muss.  
Ai-cr soll helfen, diese früh zu fangen – lokal und ohne dass der Code irgendwo hochgeladen wird.

## Status
- In Entwicklung  
- MVP: CLI + Ollama + Diff-Analyse  
- Ziel: Pre-Commit + einfache Regeln

Feedback, Issues oder Pull Requests sind super willkommen! 🚀

## Wie mitmachen / ausprobieren
(Bald: Install-Anleitung hier)

Lizenz: MIT
