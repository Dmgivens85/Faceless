from __future__ import annotations

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Breakdown
from app.schemas import BreakdownInput
from app.services.ai_service import ai_service
from app.services.markdown_export import breakdown_to_markdown
from app.utils.formatting import dump_list


router = APIRouter()


@router.get("/breakdown-builder")
def breakdown_builder_page(request: Request):
    templates = request.app.state.templates
    return templates.TemplateResponse(
        "breakdown_builder.html",
        {"request": request, "page_title": "Breakdown Builder", "result": None},
    )


@router.post("/breakdown-builder")
def breakdown_builder_submit(
    request: Request,
    title: str = Form(...),
    scene: str = Form(...),
    hook: str = Form(...),
    main_analysis_points: str = Form(...),
    target_length: str = Form(...),
    db: Session = Depends(get_db),
):
    templates = request.app.state.templates
    payload = BreakdownInput(
        title=title,
        scene=scene,
        hook=hook,
        main_analysis_points=main_analysis_points,
        target_length=target_length,
    )
    result = ai_service.generate_breakdown(payload)
    breakdown = Breakdown(
        title=payload.title,
        scene=payload.scene,
        hook=payload.hook,
        main_analysis_points=payload.main_analysis_points,
        target_length=payload.target_length,
        short_video_script=result.short_video_script,
        beat_by_beat_structure=dump_list(result.beat_by_beat_structure),
        on_screen_text_suggestions=dump_list(result.on_screen_text_suggestions),
        sound_design_notes=dump_list(result.sound_design_notes),
        alternate_angle=result.alternate_angle,
    )
    db.add(breakdown)
    db.commit()
    db.refresh(breakdown)

    return templates.TemplateResponse(
        "breakdown_builder.html",
        {
            "request": request,
            "page_title": "Breakdown Builder",
            "result": result,
            "saved_id": breakdown.id,
            "provider_mode": ai_service.provider_mode,
        },
    )


@router.get("/breakdown-builder/{breakdown_id}/markdown", response_class=PlainTextResponse)
def export_breakdown_markdown(breakdown_id: int, db: Session = Depends(get_db)):
    breakdown = db.get(Breakdown, breakdown_id)
    if not breakdown:
        return PlainTextResponse("Breakdown not found.", status_code=404)
    return PlainTextResponse(
        breakdown_to_markdown(breakdown),
        headers={"Content-Disposition": f'attachment; filename="breakdown-{breakdown_id}.md"'},
    )
