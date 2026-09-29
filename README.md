# 🤖 Agency Agents Directory

A browsable website for the [agency-agents](https://github.com/msitarzewski/agency-agents)
open-source collection — **279 specialist AI agents** across 18 divisions
(Engineering, Marketing, Finance, Design, Healthcare, …), MIT licensed.

Features: text search across names/descriptions/topics, filter by division,
paginated results, and each agent's full instructions readable on one click,
with a link back to its source file on GitHub.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open http://localhost:8501 in your browser.

## Deploy on Streamlit Community Cloud (free)

You need a GitHub account. Do these steps once:

1. **Create a new repository** on GitHub (e.g. `agency-agents-site`). Public or private — both work.
2. **Upload this folder's files** to that repository: `app.py`, `requirements.txt`,
   `agents.json`, `README.md`. (On github.com: open the repo → *Add file* →
   *Upload files* → drag all four files in → *Commit changes*.)
3. Go to **https://share.streamlit.io** and sign in with GitHub.
4. Click **"Create app"** → choose your repository, branch `main`,
   and set **Main file path** to `app.py`.
5. Click **Deploy**. First deploy takes 2–5 minutes. You get a free public URL
   like `https://your-app-name.streamlit.app`.

Notes:
- No API keys or secrets needed — the site is a static directory, everything is free.
- To refresh the agent data later: re-run the parse step against a fresh clone of
  agency-agents, replace `agents.json`, and push to GitHub — Streamlit redeploys automatically.

## Files

| File | What it is |
|---|---|
| `app.py` | The Streamlit app |
| `agents.json` | All 279 agents parsed from agency-agents (names, descriptions, divisions, full instructions) |
| `requirements.txt` | Python dependencies (`streamlit` only) |
| `README.md` | This file |

## Credit

Agent data © [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) (MIT).
