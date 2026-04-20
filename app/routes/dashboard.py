from __future__ import annotations

from fastapi import APIRouter, Depends, Request
from sqlalchemy import desc, func, select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Breakdown, HookSet, PlannedPost, SceneIdea


router = APIRouter()


@router.get("/")
def dashboard(request: Request, db: Session = Depends(get_db)):
    templates = request.app.state.templates
    recent_ideas = db.scalars(select(SceneIdea).order_by(desc(SceneIdea.created_at)).limit(5)).all()
    recent_hooks = db.scalars(select(HookSet).order_by(desc(HookSet.created_at)).limit(5)).all()
    recent_breakdowns = db.scalars(select(Breakdown).order_by(desc(Breakdown.created_at)).limit(5)).all()
    planned_posts = db.scalars(select(PlannedPost).order_by(desc(PlannedPost.created_at)).limit(6)).all()

    summary = {
        "scene_ideas": db.scalar(select(func.count(SceneIdea.id))) or 0,
        "hook_sets": db.scalar(select(func.count(HookSet.id))) or 0,
        "breakdowns": db.scalar(select(func.count(Breakdown.id))) or 0,
        "planned_posts": db.scalar(select(func.count(PlannedPost.id))) or 0,
    }

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "summary": summary,
            "recent_ideas": recent_ideas,
            "recent_hooks": recent_hooks,
            "recent_breakdowns": recent_breakdowns,
            "planned_posts": planned_posts,
            "page_title": "Dashboard",
        },
    )
