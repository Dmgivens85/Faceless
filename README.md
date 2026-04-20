# Faceless

SceneSound OS is the first product inside the `Faceless` repository: a serious internal content operating system for researching, scripting, and planning faceless short-form video content about movie and TV scenes where sound drives emotional impact.

## Project Purpose

This app is designed for film-sound analysis and repeatable short-form publishing. It helps turn scene observations into usable content assets for TikTok, Instagram Reels, and YouTube Shorts without forcing you into a generic SaaS workflow.

## Features

- Dashboard with recent ideas, hooks, breakdowns, and planned posts
- Scene Finder for angle generation and sound-focused scene analysis
- Hook Writer for hooks, overlays, captions, and CTAs
- Breakdown Builder for short-form scripts, beat structure, edit notes, and Markdown export
- Content Planner with filtering and search
- Idea Vault to search across saved scene ideas, hook sets, and breakdowns
- Mock AI outputs when no API key is configured
- SQLite-backed persistence for local-first development

## Routes

- `GET /` dashboard
- `GET|POST /scene-finder`
- `GET|POST /hook-writer`
- `GET|POST /breakdown-builder`
- `GET /breakdown-builder/{breakdown_id}/markdown`
- `GET|POST /content-planner`
- `GET /ideas`

## Tech Stack

- Python
- FastAPI
- Jinja2 server-rendered templates
- SQLite
- Minimal JavaScript

## Folder Structure

```text
Faceless/
├── app/
├── data/
├── scripts/
├── static/
├── templates/
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Local Setup

1. Create and enter the repo:

   ```bash
   cd Faceless
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Copy environment variables:

   ```bash
   cp .env.example .env
   ```

4. Start the app with uvicorn:

   ```bash
   uvicorn app.main:app --reload
   ```

   Or use the local launcher:

   ```bash
   ./run.sh
   ```

   Or with `make`:

   ```bash
   make run
   ```

5. Open:

   ```text
   http://127.0.0.1:8000
   ```

## Environment Variables

- `DATABASE_URL`: SQLite database location for local development
- `OPENAI_API_KEY`: optional, reserved for future live AI integration
- `OPENAI_MODEL`: optional provider model name

If no API key is set, SceneSound OS uses structured mock outputs so the app remains fully usable.

## Seeding

The app auto-creates tables and seeds example data on startup. You can also run:

```bash
python scripts/bootstrap_db.py
```

## Suggested GitHub Repo Description

`SceneSound OS inside Faceless: a FastAPI content operating system for researching, scripting, and planning sound-driven movie and TV scene breakdowns.`

## Suggested First Commit Message

`Initial scaffold for Faceless with SceneSound OS FastAPI app`
