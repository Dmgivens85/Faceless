from __future__ import annotations

from dataclasses import asdict

from app.config import settings
from app.schemas import (
    BreakdownInput,
    BreakdownOutput,
    HookWriterInput,
    HookWriterOutput,
    SceneFinderInput,
    SceneFinderOutput,
)
from app.services.prompts import (
    build_breakdown_prompt,
    build_hook_writer_prompt,
    build_scene_finder_prompt,
)


class SceneSoundAIService:
    """Structured content generation with a clean seam for future provider integration."""

    def __init__(self, api_key: str = "") -> None:
        self.api_key = api_key or settings.openai_api_key

    @property
    def provider_mode(self) -> str:
        return "configured-fallback" if self.api_key else "mock"

    def generate_scene_analysis(self, payload: SceneFinderInput) -> SceneFinderOutput:
        prompt = build_scene_finder_prompt(payload)
        _ = prompt
        return self._mock_scene_analysis(payload)

    def generate_hook_set(self, payload: HookWriterInput) -> HookWriterOutput:
        prompt = build_hook_writer_prompt(payload)
        _ = prompt
        return self._mock_hook_set(payload)

    def generate_breakdown(self, payload: BreakdownInput) -> BreakdownOutput:
        prompt = build_breakdown_prompt(payload)
        _ = prompt
        return self._mock_breakdown(payload)

    def _mock_scene_analysis(self, payload: SceneFinderInput) -> SceneFinderOutput:
        title = payload.title
        focus = payload.sound_focus_category.lower()
        mood = payload.mood.lower()
        return SceneFinderOutput(
            why_sound_matters=[
                f"The {focus} controls what the audience notices first, steering the emotional read of {title}.",
                f"The scene gains tension because the soundtrack withholds comfort and lets the room tone do dramatic work.",
                f"Sound cues reshape performance details, making pauses, breaths, or off-screen movement feel intentional.",
                f"The mix turns the scene from plot delivery into a felt experience by emphasizing texture over exposition.",
                f"The sonic choices sharpen the contrast between what the characters say and what the atmosphere implies.",
            ],
            audience_explanations=[
                f"This scene hits because the sound tells you how uneasy the moment really is before the characters do.",
                f"You feel pulled into the scene because the audio makes the space feel alive, not just the dialogue.",
                f"The emotion lands harder because the sound design quietly tells you something is off.",
            ],
            technical_explanations=[
                f"The scene uses {focus} to manage negative space, which lets micro-details carry dramatic weight.",
                f"The balance between foreground dialogue and environmental texture creates a controlled {mood} pressure.",
                "Selective restraint in the mix leaves enough headroom for silence and ambience to function as narrative signals.",
            ],
            tags=[
                title,
                payload.sound_focus_category,
                payload.mood,
                "scene analysis",
                "sound-driven storytelling",
                "faceless shorts",
            ],
        )

    def _mock_hook_set(self, payload: HookWriterInput) -> HookWriterOutput:
        title = payload.title
        scene = payload.scene_name
        key_sound = payload.key_sound_element
        takeaway = payload.takeaway
        tone = payload.tone.lower()
        hooks = [
            f"This {title} scene only works because of one sound choice.",
            f"Everyone remembers the image in {scene}, but the audio does the real damage.",
            f"The most important part of this {title} scene is what you barely hear.",
            f"If you mute this {title} scene, it loses half its meaning.",
            f"This is how {key_sound} turns a scene into a threat.",
            f"The sound in this scene is doing way more storytelling than the dialogue.",
            f"This {title} moment feels unforgettable because the mix never lets you relax.",
            f"One audio detail completely changes how this scene reads.",
            f"The scene sounds simple, but it is engineered for emotional control.",
            f"This is why the sound of {scene} stays with you longer than the line reading.",
        ]
        overlays = [
            f"The sound is the real plot twist",
            f"Why this scene feels so tense",
            f"What the audio is really doing",
            f"The mix changes everything",
            f"{key_sound}: the hidden story engine",
        ]
        captions = [
            f"Breaking down how {title} uses sound to sell {takeaway}.",
            f"Scene study: {scene}, where {key_sound} does the emotional heavy lifting.",
            f"A quick sound-analysis pass on why this moment from {title} feels so controlled.",
        ]
        ctas = [
            f"Want more {tone} scene breakdowns like this?",
            "Comment a film or show scene I should analyze next.",
            "Follow for more sound-first breakdowns of movie and TV scenes.",
        ]
        return HookWriterOutput(
            hook_options=hooks,
            overlay_options=overlays,
            caption_starters=captions,
            cta_endings=ctas,
        )

    def _mock_breakdown(self, payload: BreakdownInput) -> BreakdownOutput:
        return BreakdownOutput(
            short_video_script=(
                f"Hook: {payload.hook}\n\n"
                f"In {payload.title}, the {payload.scene} scene works because sound carries the subtext. "
                f"Start by framing the key idea: {payload.main_analysis_points}. "
                "Then point out how the mix, ambience, and silence shape tension before the audience even processes the dialogue. "
                "Close by connecting that sonic choice to why the scene stays emotionally sticky in a short-form explanation."
            ),
            beat_by_beat_structure=[
                "Open with the hook over the most emotionally loaded visual beat.",
                "Name the scene and immediately state the key sound element.",
                "Explain how the sound changes the audience's reading of the moment.",
                "Add one technical observation about mix, silence, ambience, or diegetic detail.",
                "End with a concise takeaway that feels usable and memorable.",
            ],
            on_screen_text_suggestions=[
                payload.hook,
                "The sound tells you how to feel first",
                "Listen to the restraint in the mix",
                "Ambience = tension",
                "This is why the scene lingers",
            ],
            sound_design_notes=[
                "Leave short pauses between lines so the point about silence can breathe.",
                "Use subtle room tone under narration instead of a constant music bed.",
                "Punch in the reference moment where the sound element becomes obvious.",
                "Keep captions editorial and minimal, not meme-styled.",
            ],
            alternate_angle=(
                "Alternate angle: frame the scene as a lesson in restraint, showing how withholding musical guidance "
                "can make the audience do more emotional work."
            ),
        )


ai_service = SceneSoundAIService()
