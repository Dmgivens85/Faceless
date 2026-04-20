from __future__ import annotations

from datetime import date

from fastapi import APIRouter, Depends, Form, Query, Request
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import PlannedPost


router = APIRouter()


@router.get("/content-planner")
def content_planner_page(
    request: Request,
    search: str = Query("", alias="q"),
    status: str = Query(""),
    platform: str = Query(""),
    db: Session = Depends(get_db),
):
    templates = request.app.state.templates
    query = select(PlannedPost)
    if search:
        search_term = f"%{search}%"
        query = query.where(
            or_(
                PlannedPost.post_title.ilike(search_term),
                PlannedPost.franchise_title.ilike(search_term),
                PlannedPost.notes.ilike(search_term),
            )
        )
    if status:
        query = query.where(PlannedPost.status == status)
    if platform:
        query = query.where(PlannedPost.platform == platform)

    posts = db.scalars(query.order_by(PlannedPost.publish_date.is_(None), PlannedPost.publish_date)).all()
    return templates.TemplateResponse(
        "content_planner.html",
        {
            "request": request,
            "page_title": "Content Planner",
            "posts": posts,
            "filters": {"q": search, "status": status, "platform": platform},
        },
    )


@router.post("/content-planner")
def content_planner_submit(
    request: Request,
    post_title: str = Form(...),
    franchise_title: str = Form(...),
    format_type: str = Form(...),
    status: str = Form(...),
    platform: str = Form(...),
    publish_date: str = Form(""),
    notes: str = Form(""),
    db: Session = Depends(get_db),
):
    templates = request.app.state.templates
    parsed_date = date.fromisoformat(publish_date) if publish_date else None
    post = PlannedPost(
        post_title=post_title,
        franchise_title=franchise_title,
        format_type=format_type,
        status=status,
        platform=platform,
        publish_date=parsed_date,
        notes=notes,
    )
    db.add(post)
    db.commit()

    posts = db.scalars(select(PlannedPost).order_by(PlannedPost.publish_date.is_(None), PlannedPost.publish_date)).all()
    return templates.TemplateResponse(
        "content_planner.html",
        {
            "request": request,
            "page_title": "Content Planner",
            "posts": posts,
            "filters": {"q": "", "status": "", "platform": ""},
            "saved": True,
        },
    )
