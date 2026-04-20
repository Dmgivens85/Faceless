from __future__ import annotations

from app.models import Breakdown
from app.utils.formatting import load_list


def breakdown_to_markdown(breakdown: Breakdown) -> str:
    beats = load_list(breakdown.beat_by_beat_structure)
    overlays = load_list(breakdown.on_screen_text_suggestions)
    notes = load_list(breakdown.sound_design_notes)

    return "\n".join(
        [
            f"# {breakdown.title}",
            "",
            f"**Scene:** {breakdown.scene}",
            f"**Target Length:** {breakdown.target_length}",
            "",
            "## Hook",
            breakdown.hook,
            "",
            "## Short Video Script",
            breakdown.short_video_script,
            "",
            "## Beat-by-Beat Structure",
            *(f"- {beat}" for beat in beats),
            "",
            "## On-Screen Text Suggestions",
            *(f"- {overlay}" for overlay in overlays),
            "",
            "## Sound Design / Edit Notes",
            *(f"- {note}" for note in notes),
            "",
            "## Alternate Angle",
            breakdown.alternate_angle or "None",
            "",
        ]
    )
