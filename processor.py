import unicodedata
import re

def normalize_text(text: str) -> str:
    """Normalize unicode characters using NFKC and lowercase."""
    return unicodedata.normalize("NFKC", text).lower().strip()

def tokenize(text: str) -> list[str]:
    """Basic whitespace tokenizer (to be extended for punctuation-aware matching)."""
    cleaned = normalize_text(text)
    return [t for t in re.split(r"\s+", cleaned) if t]

def process_resume(resume_data: dict, job_text: str) -> dict:
    """Base resume processing entry point (currently lacks alias normalization, date merging, and deterministic ranking)."""
    job_tokens = set(tokenize(job_text))
    return {
        "name": resume_data.get("name", ""),
        "job_tokens": list(job_tokens),
        "selected_bullets": []
    }
