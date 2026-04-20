from __future__ import annotations

from datetime import date, datetime

from sqlalchemy import Date, DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )


class SceneIdea(TimestampMixin, Base):
    __tablename__ = "scene_ideas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), index=True)
    scene_description: Mapped[str] = mapped_column(Text)
    sound_focus_category: Mapped[str] = mapped_column(String(120), index=True)
    mood: Mapped[str] = mapped_column(String(120), index=True)
    notes: Mapped[str] = mapped_column(Text, default="", nullable=False)
    why_sound_matters: Mapped[str] = mapped_column(Text)
    audience_explanations: Mapped[str] = mapped_column(Text)
    technical_explanations: Mapped[str] = mapped_column(Text)
    tags: Mapped[str] = mapped_column(Text, default="", nullable=False)


class HookSet(TimestampMixin, Base):
    __tablename__ = "hook_sets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), index=True)
    scene_name: Mapped[str] = mapped_column(String(255))
    key_sound_element: Mapped[str] = mapped_column(String(255), index=True)
    takeaway: Mapped[str] = mapped_column(Text)
    tone: Mapped[str] = mapped_column(String(120), index=True)
    hook_options: Mapped[str] = mapped_column(Text)
    overlay_options: Mapped[str] = mapped_column(Text)
    caption_starters: Mapped[str] = mapped_column(Text)
    cta_endings: Mapped[str] = mapped_column(Text)


class Breakdown(TimestampMixin, Base):
    __tablename__ = "breakdowns"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), index=True)
    scene: Mapped[str] = mapped_column(String(255), index=True)
    hook: Mapped[str] = mapped_column(Text)
    main_analysis_points: Mapped[str] = mapped_column(Text)
    target_length: Mapped[str] = mapped_column(String(80))
    short_video_script: Mapped[str] = mapped_column(Text)
    beat_by_beat_structure: Mapped[str] = mapped_column(Text)
    on_screen_text_suggestions: Mapped[str] = mapped_column(Text)
    sound_design_notes: Mapped[str] = mapped_column(Text)
    alternate_angle: Mapped[str] = mapped_column(Text, default="", nullable=False)


class PlannedPost(TimestampMixin, Base):
    __tablename__ = "planned_posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    post_title: Mapped[str] = mapped_column(String(255), index=True)
    franchise_title: Mapped[str] = mapped_column(String(255), index=True)
    format_type: Mapped[str] = mapped_column(String(80), index=True)
    status: Mapped[str] = mapped_column(String(80), index=True)
    platform: Mapped[str] = mapped_column(String(80), index=True)
    publish_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    notes: Mapped[str] = mapped_column(Text, default="", nullable=False)
