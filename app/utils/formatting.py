from __future__ import annotations


def dump_list(items: list[str]) -> str:
    return "\n".join(item.strip() for item in items if item and item.strip())


def load_list(raw: str) -> list[str]:
    return [line.strip() for line in raw.splitlines() if line.strip()]


def clip_words(text: str, limit: int = 24) -> str:
    words = text.split()
    if len(words) <= limit:
        return text
    return " ".join(words[:limit]).rstrip() + "..."
