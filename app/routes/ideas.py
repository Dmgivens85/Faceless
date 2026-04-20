from __future__ import annotations

from fastapi import APIRouter, Depends, Query, Request
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Breakdown, HookSet, SceneIdea
from app.utils.formatting import clip_words


router = APIRouter()


@router.get("/ideas")
def idea_vault_page(
    request: Request,
    q: str = Query(""),
    category: str = Query(""),
    mood: str = Query(""),
    db: Session = Depends(get_db),
):
    templates = request.app.state.templates
    idea_query = select(SceneIdea)
    if q:
        term = f"%{q}%"
        idea_query = idea_query.where(
            or_(
                SceneIdea.title.ilike(term),
                SceneIdea.scene_description.ilike(term),
                SceneIdea.tags.ilike(term),
                SceneIdea.notes.ilike(term),
            )
        )
    if category:
        idea_query = idea_query.where(SceneIdea.sound_focus_category == category)
    if mood:
        idea_query = idea_query.where(SceneIdea.mood == mood)

    scene_ideas = db.scalars(idea_query.order_by(SceneIdea.created_at.desc())).all()

    hook_query = select(HookSet)
    breakdown_query = select(Breakdown)
    if q:
        term = f"%{q}%"
        hook_query = hook_query.where(
            or_(HookSet.title.ilike(term), HookSet.scene_name.ilike(term), HookSet.key_sound_element.ilike(term))
        )
        breakdown_query = breakdown_query.where(
            or_(Breakdown.title.ilike(term), Breakdown.scene.ilike(term), Breakdown.hook.ilike(term))
        )

    hook_sets = db.scalars(hook_query.order_by(HookSet.created_at.desc())).all()
    breakdowns = db.scalars(breakdown_query.order_by(Breakdown.created_at.desc())).all()

    combined = [
        {
            "type": "Scene Idea",
            "title": item.title,
            "context": f"{item.sound_focus_category} · {item.mood}",
            "summary": clip_words(item.scene_description, 28),
        }
        for item in scene_ideas
    ] + [
        {
            "type": "Hook Set",
            "title": item.title,
            "context": f"{item.scene_name} · {item.tone}",
            "summary": clip_words(item.takeaway, 28),
        }
        for item in hook_sets
    ] + [
        {
            "type": "Breakdown",
            "title": item.title,
            "context": f"{item.scene} · {item.target_length}",
            "summary": clip_words(item.hook, 28),
        }
        for item in breakdowns
    ]

    categories = sorted({idea.sound_focus_category for idea in db.scalars(select(SceneIdea)).all()})
    moods = sorted({idea.mood for idea in db.scalars(select(SceneIdea)).all()})

    return templates.TemplateResponse(
        "ideas.html",
        {
            "request": request,
            "page_title": "Idea Vault",
            "entries": combined,
            "filters": {"q": q, "category": category, "mood": mood},
            "categories": categories,
            "moods": moods,
        },
    )
