from __future__ import annotations

from fastapi import APIRouter, Request

from app.creator_toolkit import (
    CAPTION_FRAMEWORK,
    CONTENT_PILLARS,
    HOOK_FORMULAS,
    HOUSE_THESIS,
    STARTER_TOPICS,
    WORKFLOW_STEPS,
)


router = APIRouter()


@router.get("/creator-toolkit")
def creator_toolkit_page(request: Request):
    templates = request.app.state.templates
    return templates.TemplateResponse(
        "creator_toolkit.html",
        {
            "request": request,
            "page_title": "Creator Toolkit",
            "house_thesis": HOUSE_THESIS,
            "pillars": CONTENT_PILLARS,
            "hook_formulas": HOOK_FORMULAS,
            "caption_framework": CAPTION_FRAMEWORK,
            "starter_topics": STARTER_TOPICS,
            "workflow_steps": WORKFLOW_STEPS,
        },
    )
