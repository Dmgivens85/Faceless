from __future__ import annotations

from fastapi import APIRouter, Depends, Form, Request
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import HookSet
from app.schemas import HookWriterInput
from app.services.ai_service import ai_service
from app.utils.formatting import dump_list


router = APIRouter()


@router.get("/hook-writer")
def hook_writer_page(request: Request):
    templates = request.app.state.templates
    return templates.TemplateResponse(
        "hook_writer.html",
        {"request": request, "page_title": "Hook Writer", "result": None},
    )


@router.post("/hook-writer")
def hook_writer_submit(
    request: Request,
    title: str = Form(...),
    scene_name: str = Form(...),
    key_sound_element: str = Form(...),
    takeaway: str = Form(...),
    tone: str = Form(...),
    db: Session = Depends(get_db),
):
    templates = request.app.state.templates
    payload = HookWriterInput(
        title=title,
        scene_name=scene_name,
        key_sound_element=key_sound_element,
        takeaway=takeaway,
        tone=tone,
    )
    result = ai_service.generate_hook_set(payload)
    hook_set = HookSet(
        title=payload.title,
        scene_name=payload.scene_name,
        key_sound_element=payload.key_sound_element,
        takeaway=payload.takeaway,
        tone=payload.tone,
        hook_options=dump_list(result.hook_options),
        overlay_options=dump_list(result.overlay_options),
        caption_starters=dump_list(result.caption_starters),
        cta_endings=dump_list(result.cta_endings),
    )
    db.add(hook_set)
    db.commit()
    db.refresh(hook_set)

    return templates.TemplateResponse(
        "hook_writer.html",
        {
            "request": request,
            "page_title": "Hook Writer",
            "result": result,
            "saved_id": hook_set.id,
            "provider_mode": ai_service.provider_mode,
        },
    )
