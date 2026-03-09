# Ai-cr - AI Change Reviewer

A small, **local-first** tool that reviews **AI-generated code** (from Cursor, Claude, Copilot, Aider, Windsurf, etc.) **before** you commit.

### Features (planned / in progress)
- Detects typical AI-specific mistakes  
  (hallucinations, subtle bugs, over-refactoring, inconsistent error handling, security issues, etc.)
- Runs completely offline using Ollama  
  (no cloud calls, no API costs, no data privacy risks)
- Can be used as a pre-commit hook
- Interactive mode (suggest fixes or ignore certain patterns)
- Still very early stage – MVP coming soon!

### Why this tool?
AI coding assistants make us faster on simple tasks, but they often introduce hard-to-spot bugs in complex or legacy code.  
Ai-cr helps catch these issues **early** and **locally** – without sending your code anywhere.

### Current status
- In development  
- Goal for MVP: simple CLI + Ollama integration + git diff analysis  
- Feedback, issues, stars and pull requests are very welcome! 🚀

### How to try / contribute
(Installation instructions coming soon)

License: MIT
