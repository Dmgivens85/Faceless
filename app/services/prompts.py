from __future__ import annotations

from app.schemas import BreakdownInput, HookWriterInput, SceneFinderInput


def build_scene_finder_prompt(payload: SceneFinderInput) -> str:
    return (
        "Analyze a film or television scene through the lens of sound. "
        f"Title: {payload.title}. Scene: {payload.scene_description}. "
        f"Sound focus: {payload.sound_focus_category}. Mood: {payload.mood}. "
        f"Notes: {payload.notes or 'None'}."
    )


def build_hook_writer_prompt(payload: HookWriterInput) -> str:
    return (
        "Write social hooks for a faceless film-sound breakdown account. "
        f"Title: {payload.title}. Scene: {payload.scene_name}. "
        f"Sound element: {payload.key_sound_element}. Takeaway: {payload.takeaway}. "
        f"Tone: {payload.tone}."
    )


def build_breakdown_prompt(payload: BreakdownInput) -> str:
    return (
        "Turn a scene analysis into a short-form editorial breakdown script. "
        f"Title: {payload.title}. Scene: {payload.scene}. Hook: {payload.hook}. "
        f"Main points: {payload.main_analysis_points}. Target length: {payload.target_length}."
    )
