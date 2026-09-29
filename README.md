# CrewAI Hands-On Exercises (CodeSandbox-ready)

Learn **multi-agent collaboration (Crews)** and **workflow orchestration (Flows)** with CrewAI 1.x × Google Gemini, by writing code yourself. Each exercise is an **independent folder** that runs as-is on CodeSandbox.

## Getting started on CodeSandbox

1. Upload/import this folder (or its zip) into CodeSandbox
   ([codesandbox.io](https://codesandbox.io) → Create → Import, then drag and drop the zip)
2. Get a Gemini API key — [Google AI Studio](https://aistudio.google.com/apikey) (**no credit card, free tier**)
3. Give CodeSandbox your API key, using one of the two methods below

### Method A: Env Variables (★ recommended for public sandboxes)

CodeSandbox sandboxes are **public** by default in some cases. Writing your key into a file
(`.env`) risks exposing it to anyone who opens the sandbox, so the safe route is to
**register it under Env Variables and never put it in a file.**

1. In the left sidebar, open **Server Control Panel** (the gear/server icon) → **Env Variables**
   (or the **Env** tab in the left panel)
2. Add this single entry
   - **Name:** `GOOGLE_API_KEY`
   - **Value:** the API key you obtained
3. If it doesn't take effect right away, **Restart Server** (or reopen the terminal)

Env Variables registered this way are passed in as environment variables, so they are read
through `os.environ` whether or not `load_dotenv()` is present. After that, just run the exercise.

```bash
cd section1/1-2
pip install -r requirements.txt     # not needed if you already installed at the root
python exercise.py
```

### Method B: a .env file (for local or private environments)

```bash
cd section1/1-2
cp .env.example .env        # paste your key after GOOGLE_API_KEY= in .env
pip install -r requirements.txt
python exercise.py
```

> ⚠️ **Do not put a real key in `.env` in a public sandbox** — anyone can read it. If you want to
> use `.env`, do it in a private sandbox or on your local machine.
> Each exercise folder runs independently (each one includes its own `requirements.txt` and `.env.example`).
> section4 includes `config/*.yaml`; some exercises in section3 include `notes.txt` / `memo.txt` in the same folder.

## Learning flow

```
① Watch the problem walkthrough video → ② Fill in the TODOs in exercise.py → ③ Check your work against Q*.md's model answer
```

What's inside each exercise folder:

| File | Purpose |
|---|---|
| `exercise.py` | Starter code with TODOs to fill in |
| `Q*.md` | The problem statement, explanation, and model answer (answer is in a collapsible section at the end) |
| `requirements.txt` | Required packages |
| `.env.example` | Template for `GOOGLE_API_KEY=` |
| `notes.txt` / `memo.txt` | (some section3 exercises) Sample file read by a tool |
| `config/*.yaml` | (section4) Agent/Task configuration files |

## Curriculum

| Section | Theme |
|---|---|
| section1 | Crew basics (Agent / Task / Crew / inputs) |
| section2 | Multi-agent collaboration (passing results via context, output_file) |
| section3 | Tools (FileReadTool / custom @tool) |
| section4 | Externalizing config (YAML config, @CrewBase style) |
| section5 | Flows (@start / @listen / state / @router / Flow × Crew) |
| section6 | Capstone (article-generation pipeline with an approval gate in a Flow) |

## Model & packages used (important)

- LLM: `LLM(model="gemini/gemini-flash-latest")` (the `gemini/` prefix is required)
- Dependencies: `crewai[google-genai]` (the `[google-genai]` extra is required — without it the Google provider won't load and you'll get an error), `crewai-tools`, `python-dotenv`, and (section4 only) `pyyaml`

> **Python is pinned to 3.12 automatically** (specified in `.devcontainer/Dockerfile`). crewai /
> crewai-tools support only `>=3.10,<3.14`; on 3.14 the dependencies can't be resolved and
> `pip install` fails. When you import into CodeSandbox the environment is built with the 3.12 from
> the Dockerfile, so normally there is nothing for you to do (to change it, edit the
> `FROM ...python:3.12` tag in the Dockerfile).
> The Gemini free tier has **rate limits** (a handful of requests per minute, and a daily cap). Multi-agent runs call the API multiple times per execution, so if you see `429 RESOURCE_EXHAUSTED`, wait a few seconds to a few minutes and try again — it's not a bug in your code.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `ModuleNotFoundError: crewai` | Check that you ran `pip install -r requirements.txt` |
| `Google Gen AI native provider not available` | Reinstall with `crewai[google-genai]` (the `[google-genai]` extra is required) |
| `API key not valid` | Check `GOOGLE_API_KEY` (registered under Env Variables / written into `.env`, and no typo in the pasted value) |
| `429 RESOURCE_EXHAUSTED` | Free-tier rate limit. Wait a bit and retry |
| `NameError` (when running the starter as-is) | Implement the TODOs in `exercise.py` first — running it unfinished raises an undefined-variable error |
