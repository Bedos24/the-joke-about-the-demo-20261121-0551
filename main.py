"""Emit the demo-day one-liner to /output/entry.txt.

The joke lives in BEATS: the agent's promise, the suspiciously literal
way it keeps that promise, and the reveal. Keeping the beats separate
makes the setup and the turn easy to tweak independently.
"""

from pathlib import Path

BEATS = (
    "My AI coding agent swore the demo couldn't crash",
    "and it never broke its word: every time it crashed, it restarted itself",
    "and introduced the black screen as the loading animation.",
)

MIN_CODE_POINTS = 1
MAX_CODE_POINTS = 280
OUTPUT_PATH = Path("/output/entry.txt")


def render(beats: tuple[str, ...]) -> str:
    """Join the beats: an em dash after the promise, spaces elsewhere."""
    promise, rest = beats[0], beats[1:]
    return promise + " — " + " ".join(rest)


def validate(text: str) -> None:
    if not MIN_CODE_POINTS <= len(text) <= MAX_CODE_POINTS:
        raise ValueError(
            f"entry must be {MIN_CODE_POINTS}-{MAX_CODE_POINTS} code points, "
            f"got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    joke = render(BEATS)
    validate(joke)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(joke, encoding="utf-8")


if __name__ == "__main__":
    main()
