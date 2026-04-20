from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class SceneFinderInput:
    title: str
    scene_description: str
    sound_focus_category: str
    mood: str
    notes: str = ""


@dataclass(slots=True)
class HookWriterInput:
    title: str
    scene_name: str
    key_sound_element: str
    takeaway: str
    tone: str


@dataclass(slots=True)
class BreakdownInput:
    title: str
    scene: str
    hook: str
    main_analysis_points: str
    target_length: str


@dataclass(slots=True)
class SceneFinderOutput:
    why_sound_matters: list[str] = field(default_factory=list)
    audience_explanations: list[str] = field(default_factory=list)
    technical_explanations: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)


@dataclass(slots=True)
class HookWriterOutput:
    hook_options: list[str] = field(default_factory=list)
    overlay_options: list[str] = field(default_factory=list)
    caption_starters: list[str] = field(default_factory=list)
    cta_endings: list[str] = field(default_factory=list)


@dataclass(slots=True)
class BreakdownOutput:
    short_video_script: str
    beat_by_beat_structure: list[str] = field(default_factory=list)
    on_screen_text_suggestions: list[str] = field(default_factory=list)
    sound_design_notes: list[str] = field(default_factory=list)
    alternate_angle: str = ""
