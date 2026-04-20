from __future__ import annotations

from datetime import date

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Breakdown, HookSet, PlannedPost, SceneIdea


def seed_database(db: Session) -> None:
    existing = db.scalar(select(SceneIdea.id).limit(1))
    if existing:
        return

    scene_ideas = [
        SceneIdea(
            title="The Sopranos",
            scene_description="Diner finale where Journey's 'Don't Stop Believin'' keeps playing as tension slowly sharpens before the cut to black.",
            sound_focus_category="Needle drop / suspense",
            mood="Paranoid",
            notes="Look at how the jukebox perspective and door chime build POV anxiety.",
            why_sound_matters="\n".join(
                [
                    "The song creates false familiarity while the edit keeps turning it into dread.",
                    "Every door chime resets Tony's alertness and trains the audience to scan the room.",
                    "The contrast between public-space chatter and Tony's interior threat is all in the soundscape.",
                    "The music carries suspense without overt score signposting.",
                    "The abrupt loss of all sound at the cut to black becomes the final narrative event.",
                ]
            ),
            audience_explanations="\n".join(
                [
                    "The song makes the scene feel normal, which is exactly why the danger feels worse.",
                    "You start listening for who enters because the sound keeps forcing your attention to the door.",
                    "The ending lands because sound disappears before you get emotional closure.",
                ]
            ),
            technical_explanations="\n".join(
                [
                    "The cue is mixed as lived-in source music rather than a purely editorial track.",
                    "Repetitive chimes create a hard sonic punctuation pattern that mimics threat checks.",
                    "The final blackout weaponizes silence as the last cut in the sequence.",
                ]
            ),
            tags="The Sopranos\nDon't Stop Believin'\ndiner finale\nsuspense\nneedle drop",
        ),
        SceneIdea(
            title="No Country for Old Men",
            scene_description="Anton Chigurh gas station scene where near-silence and vocal control create dread.",
            sound_focus_category="Silence / vocal restraint",
            mood="Threatening",
            notes="The scene feels dangerous because almost nothing is exaggerated.",
            why_sound_matters="Near-silence makes every line feel loaded.\nRestraint amplifies menace.\nNo score leaves the clerk exposed.\nThe room tone keeps things painfully ordinary.\nChigurh's vocal pacing becomes the weapon.",
            audience_explanations="It feels scary because the movie refuses to tell you how to feel.\nThe quiet makes every pause feel dangerous.\nThe scene sounds normal, which makes the threat feel real.",
            technical_explanations="Dialogue pacing carries dynamic tension.\nAbsence of non-diegetic score preserves realism.\nSparse ambience expands the emotional weight of pauses.",
            tags="No Country for Old Men\nsilence\ndread\ndialogue tension",
        ),
        SceneIdea(
            title="Whiplash",
            scene_description="First full rehearsal under Fletcher where room slap, stick attack, and verbal abuse become one pressure system.",
            sound_focus_category="Performance intensity",
            mood="Volatile",
            notes="Look at the collision between musical precision and emotional violence.",
            why_sound_matters="The rehearsal room acoustics make every correction feel physical.\nThe drum attacks turn performance into conflict.\nVocal humiliation and instrument tone live in the same pressure field.\nThe sound keeps escalating before the edit does.\nMusicianship becomes audible fear.",
            audience_explanations="You feel the pressure because the room sounds punishing.\nThe drumming stops sounding musical and starts sounding like stress.\nThe audio makes practice feel like combat.",
            technical_explanations="Transient-heavy percussion drives physiological tension.\nRoom reflections keep the rehearsal grounded in a believable space.\nDynamic contrast between speech and attack reinforces power imbalance.",
            tags="Whiplash\ndrums\nrehearsal\npressure",
        ),
        SceneIdea(
            title="Hereditary",
            scene_description="Telephone pole aftermath where shock is carried through absence, distance, and delayed response.",
            sound_focus_category="Trauma / negative space",
            mood="Devastated",
            notes="The restraint is what makes the moment unbearable.",
            why_sound_matters="The film avoids melodramatic scoring in the immediate aftermath.\nDistance and stillness let dread expand on its own.\nThe audience is trapped in anticipation before the reveal.\nThe quiet shifts attention to breathing and emotional paralysis.\nSound refuses to release the tension.",
            audience_explanations="It hurts because the movie doesn't rush to help you process it.\nThe silence makes you sit in shock with the character.\nYou hear grief before you fully see it.",
            technical_explanations="Negative sonic space delays catharsis.\nMinimal foreground detail emphasizes suspended reaction.\nThe withholding strategy makes the later emotional break hit harder.",
            tags="Hereditary\nsilence\nshock\ngrief",
        ),
        SceneIdea(
            title="There Will Be Blood",
            scene_description="Oil derrick sequence where industrial violence and score merge into obsession.",
            sound_focus_category="Industrial sound / score collision",
            mood="Obsessive",
            notes="The machine noise feels mythic because it never stays purely literal.",
            why_sound_matters="Mechanical noise becomes emotional storytelling.\nThe scene sounds like ambition tearing itself open.\nThe score and source texture stop feeling separate.\nScale is built through density, not dialogue.\nThe sonic chaos sells both triumph and loss.",
            audience_explanations="The scene sounds huge because the machinery becomes part of the emotion.\nYou can hear success and disaster at the same time.\nThe audio turns the oil rig into a character.",
            technical_explanations="Layered industrial texture broadens perceived scale.\nScore integration blurs literal and psychological space.\nSonic overload mirrors narrative obsession.",
            tags="There Will Be Blood\noil derrick\nindustrial sound",
        ),
        SceneIdea(
            title="Blade Runner 2049",
            scene_description="Baseline test sequences where repetition, vocal rhythm, and sub-bass flatten humanity.",
            sound_focus_category="Repetition / low-frequency control",
            mood="Clinical",
            notes="The audio feels procedural and dehumanizing on purpose.",
            why_sound_matters="Repetition erases comfort and individuality.\nLow-end pressure keeps the body tense.\nThe voice pattern feels diagnostic rather than conversational.\nMinimal variation sells institutional control.\nSound turns language into compliance.",
            audience_explanations="It feels cold because the scene sounds like a machine checking a machine.\nThe repetition keeps the audience trapped in the same rhythm.\nThe bass makes the scene feel oppressive even when nothing big happens.",
            technical_explanations="Low-frequency emphasis creates somatic pressure.\nRhythmic speech patterning drives procedural unease.\nSparse sonic variance supports the theme of dehumanization.",
            tags="Blade Runner 2049\nbaseline test\nsub bass",
        ),
        SceneIdea(
            title="A Quiet Place",
            scene_description="Nail staircase sequence where environmental detail turns movement into terror.",
            sound_focus_category="Micro-detail / survival tension",
            mood="Fragile",
            notes="Everything small matters because the world punishes sound.",
            why_sound_matters="Tiny environmental details become life-or-death events.\nThe mix teaches the audience to fear accidental noise.\nSilence is no longer peace, it is risk management.\nEvery surface has narrative value.\nSound turns domestic space into a threat map.",
            audience_explanations="The scene is tense because even a small sound feels catastrophic.\nYou start thinking about the room like a trap.\nThe audio makes ordinary movement feel dangerous.",
            technical_explanations="Micro-detail is promoted to primary narrative information.\nDynamic restraint magnifies isolated transients.\nThe sound field converts space into a survival system.",
            tags="A Quiet Place\nsilence\nsurvival tension",
        ),
        SceneIdea(
            title="The Social Network",
            scene_description="Opening bar conversation where overlapping dialogue and room noise create competitive velocity.",
            sound_focus_category="Dialogue rhythm / room realism",
            mood="Combative",
            notes="The speed is musical even before the score enters.",
            why_sound_matters="Dialogue pace creates momentum and imbalance.\nThe room keeps the scene social rather than theatrical.\nInterruptions become character evidence.\nClarity is preserved without removing friction.\nSound makes intelligence feel aggressive.",
            audience_explanations="The scene moves fast because the sound never lets the air settle.\nYou hear the mismatch between the two characters before the breakup lands.\nThe room noise keeps the conversation feeling real and unstable.",
            technical_explanations="Dialogue cadence functions like percussive structure.\nAmbient detail maintains realism while preserving intelligibility.\nInterruptive overlap reveals character asymmetry.",
            tags="The Social Network\ndialogue\noverlap",
        ),
    ]

    hook_sets = [
        HookSet(
            title="The Sopranos",
            scene_name="Diner Finale",
            key_sound_element="Door chime and source music",
            takeaway="sound can create paranoia without traditional score",
            tone="Analytical",
            hook_options="This ending is remembered for the cut, but the sound is what makes it terrifying.\nThe door chime is the real suspense engine in this Sopranos scene.",
            overlay_options="The chime keeps resetting tension\nWhy the diner sounds dangerous",
            caption_starters="A sound-first look at why the Sopranos finale feels so uneasy.",
            cta_endings="Follow for more scene sound breakdowns.",
        ),
        HookSet(
            title="Whiplash",
            scene_name="First Fletcher Rehearsal",
            key_sound_element="Drum attack and room slap",
            takeaway="performance sound can become psychological violence",
            tone="Intense",
            hook_options="This rehearsal sounds like a fight scene.\nWhiplash turns practice into pressure through sound alone.",
            overlay_options="This room sounds brutal\nWhen music becomes threat",
            caption_starters="Breaking down how Whiplash weaponizes rehearsal sound.",
            cta_endings="Comment the next scene to analyze.",
        ),
    ]

    breakdowns = [
        Breakdown(
            title="The Sopranos Finale Sound Breakdown",
            scene="Holsten's diner finale",
            hook="The scariest part of the Sopranos ending is not the cut to black. It's the sound that trains you to fear it.",
            main_analysis_points="door chime repetition, source music familiarity, cut to silence",
            target_length="45 seconds",
            short_video_script="Open on the diner door. Explain that every chime makes Tony, and us, re-scan the room. Point out how 'Don't Stop Believin'' feels casual until repetition turns it uncanny. End by landing on the blackout as a sound event, not just an edit.",
            beat_by_beat_structure="Open with the chime.\nName the scene and why people misremember the tension source.\nExplain how the song and chime create alertness.\nClose on silence as the final blow.",
            on_screen_text_suggestions="The sound trains your paranoia\nDoor chime = threat reset\nThe silence is the ending",
            sound_design_notes="Keep the intro quiet.\nLet the chime breathe between lines.\nAvoid over-scoring the explanation.",
            alternate_angle="Frame it as a lesson in POV sound design for suspense.",
        ),
        Breakdown(
            title="No Country Gas Station Breakdown",
            scene="Gas station coin toss",
            hook="This scene proves silence can be more threatening than music.",
            main_analysis_points="vocal restraint, no score, deadly pauses",
            target_length="30 seconds",
            short_video_script="Introduce the idea that nothing is exaggerated. Walk through how Chigurh's stillness and vocal control make every pause feel armed. Close by noting that the lack of score prevents emotional distance.",
            beat_by_beat_structure="State the core idea.\nPoint to silence.\nPoint to pacing.\nConnect it to realism-driven dread.",
            on_screen_text_suggestions="Silence as threat\nNo score, no safety\nPacing does the violence",
            sound_design_notes="Use room tone under the whole read.\nLeave a beat after the word silence.",
            alternate_angle="Explain it as anti-Hollywood suspense design.",
        ),
    ]

    planned_posts = [
        PlannedPost(
            post_title="Why the Sopranos finale sounds so dangerous",
            franchise_title="The Sopranos",
            format_type="Scene Breakdown",
            status="Draft",
            platform="TikTok",
            publish_date=date(2026, 4, 22),
            notes="Lead with the door chime. Keep captions restrained.",
        ),
        PlannedPost(
            post_title="No score, maximum dread in No Country",
            franchise_title="No Country for Old Men",
            format_type="Audio Analysis",
            status="Planned",
            platform="YouTube Shorts",
            publish_date=date(2026, 4, 24),
            notes="Use a quiet room tone bed for narration.",
        ),
        PlannedPost(
            post_title="Why Whiplash rehearsal scenes feel violent",
            franchise_title="Whiplash",
            format_type="Hook Test",
            status="Research",
            platform="Instagram Reels",
            publish_date=None,
            notes="Could become a recurring music-performance analysis series.",
        ),
    ]

    db.add_all(scene_ideas + hook_sets + breakdowns + planned_posts)
    db.commit()
