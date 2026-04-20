from __future__ import annotations

from fastapi import APIRouter, Depends, Form, Request
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import SceneIdea
from app.schemas import SceneFinderInput
from app.services.ai_service import ai_service
from app.utils.formatting import dump_list


router = APIRouter()


@router.get("/scene-finder")
def scene_finder_page(request: Request):
    templates = request.app.state.templates
    return templates.TemplateResponse(
        "scene_finder.html",
        {"request": request, "page_title": "Scene Finder", "result": None},
    )


@router.post("/scene-finder")
def scene_finder_submit(
    request: Request,
    title: str = Form(...),
    scene_description: str = Form(...),
    sound_focus_category: str = Form(...),
    mood: str = Form(...),
    notes: str = Form(""),
    db: Session = Depends(get_db),
):
    templates = request.app.state.templates
    payload = SceneFinderInput(
        title=title,
        scene_description=scene_description,
        sound_focus_category=sound_focus_category,
        mood=mood,
        notes=notes,
    )
    result = ai_service.generate_scene_analysis(payload)
    idea = SceneIdea(
        title=payload.title,
        scene_description=payload.scene_description,
        sound_focus_category=payload.sound_focus_category,
        mood=payload.mood,
        notes=payload.notes,
        why_sound_matters=dump_list(result.why_sound_matters),
        audience_explanations=dump_list(result.audience_explanations),
        technical_explanations=dump_list(result.technical_explanations),
        tags=dump_list(result.tags),
    )
    db.add(idea)
    db.commit()
    db.refresh(idea)

    return templates.TemplateResponse(
        "scene_finder.html",
        {
            "request": request,
            "page_title": "Scene Finder",
            "result": result,
            "saved_id": idea.id,
            "provider_mode": ai_service.provider_mode,
        },
    )
