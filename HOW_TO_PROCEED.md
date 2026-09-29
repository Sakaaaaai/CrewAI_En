# How to Work Through the Exercises (CrewAI 1.x)

---

## The overall flow

```
① Watch the problem walkthrough video
        ↓
② Write code in CodeSandbox
        ↓
③ Check your work against the solution video
```

This course is a follow-up (or companion) to the **LangChain course, which goes deep on a single agent**.
Here, you'll get hands-on with **multi-agent collaboration (Crews) and workflow orchestration (Flows)**.

---

## ① Watch the problem walkthrough video

- Confirm the concept and goal for today
- Get a feel for the structure of the starter code (`exercise.py`)
- Picture "what kind of team (Crew) / what kind of flow (Flow) am I building" before you start typing

---

## ② Write code in CodeSandbox

- A dev environment that runs entirely in your browser (nothing to install)
- Implement the sections marked with `TODO` comments in `exercise.py`
- Run `python exercise.py` in the terminal as you go
- **Try it on your own for at least 5 minutes, even if you're stuck** (pause the video and give it a shot!)

---

## ③ Check your work against the solution video

- Compare your code with the model answer
- Don't stop at "it runs" — make sure you can explain "why split roles this way" or "why use a Flow here"
- Each exercise's `Q*.md` has a **model answer** at the end

---

## Setting up your API key (one-time only)

1. Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey) (**no credit card, free tier**)
2. Rename each exercise folder's `.env.example` to `.env`
3. Paste your key after `GOOGLE_API_KEY=`

```
# .env
GOOGLE_API_KEY=AIzaSy...(your key)
```

> Keep your API key in `.env` — never hard-code it into your source files.
> CrewAI's built-in Google GenAI provider picks up `GOOGLE_API_KEY` automatically.

---

## About the model we use

This course uses **`gemini/gemini-flash-latest`** (a stable alias that always points to the latest Flash model).

```python
from crewai import LLM
llm = LLM(model="gemini/gemini-flash-latest")
```

> You may see `gemini-2.5-flash` mentioned in the videos or slides, but that can return a 404 on newly created accounts.
> **Always use `gemini-flash-latest` in your code.**

---

## Troubleshooting

| Situation | Fix |
|---|---|
| `ModuleNotFoundError: crewai` | Check that you ran `pip install -r requirements.txt` |
| `Google Gen AI native provider not available` | `pip install "crewai[google-genai]"` |
| `... API key not valid` | Check `GOOGLE_API_KEY` in your `.env` |
| `404 ... no longer available` | Change the model name to `gemini/gemini-flash-latest` |
| `429 RESOURCE_EXHAUSTED` | Free-tier rate limit. Wait a bit and retry (multi-agent runs make more calls) |
| Not sure what the problem is asking | Rewatch the problem walkthrough video |

> **CrewAI-specific note**: more agents means more LLM calls.
> Exercises are capped at 3 agents. If you hit a 429, just wait a little and try again.

---

## Folder structure

```
exercises/
├── section1/  Agent and Task basics
├── section2/  Multi-agent collaboration (Crews)
├── section3/  Connecting to the outside world with tools
├── section4/  YAML config and project structure
├── section5/  Flows — controlled workflows
└── section6/  Capstone project (blog-post pipeline)
```

Each exercise folder generally contains:

| File | Purpose |
|---|---|
| `exercise.py` | Starter code with TODOs to fill in |
| `Q*.md` | Problem statement, explanation, model answer |
| `requirements.txt` | Required packages |
| `*.txt` / `config/*.yaml` | Sample material/config used by some exercises |

---

## Summary

> The goal isn't just "it works" — aim to be able to **explain why you split roles this way, and why you structured the flow this way**

Repeat ① watch → ② write → ③ check for every lecture
