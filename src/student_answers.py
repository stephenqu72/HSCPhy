import json
import os
import re


def read_json_list(path: str) -> list:
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except Exception:
        return []


def append_answer_log(path: str, entry: dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    entries = read_json_list(path)
    entries.append(dict(entry))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)


def latest_answers_by_key(entries: list) -> dict:
    latest = {}
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        key = entry.get("key")
        if not key:
            continue
        current = latest.get(key)
        if current is None or entry.get("timestamp", "") >= current.get("timestamp", ""):
            latest[key] = entry
    return latest


def build_answer_summary(entries: list, selection: list) -> dict:
    latest = latest_answers_by_key(entries)
    rows = []
    for index, item in enumerate(selection, 1):
        key = item.get("key")
        entry = latest.get(key)
        if entry is None:
            continue
        rows.append(
            {
                "Question": index,
                "Image": item.get("image", ""),
                "Type": entry.get("question_type") or item.get("question_type", ""),
                "Last answered": entry.get("timestamp", ""),
                "Answer": entry.get("answer", ""),
                "Feedback": entry.get("feedback", ""),
            }
        )
    return {
        "answered_count": len(rows),
        "total_count": len(selection),
        "rows": rows,
    }


def build_answer_feedback_prompt(question_type: str, student_answer: str, teacher_answer: str) -> str:
    return f"""
You are a supportive NSW HSC Physics tutor. Compare the student's answer with the saved teacher answer.

Question type: {question_type}

Student answer:
{student_answer}

Saved teacher answer:
{teacher_answer}

Give concise, encouraging feedback in this format:
- Result: correct, partly correct, or needs work
- What was good
- What to fix or add
- A short improved answer the student could write

Keep it student-friendly and do not be harsh.
""".strip()


def build_flash_card_prompt(saved_answer: str) -> str:
    return f"""
You are a concise NSW HSC Physics study coach. Create one flash card from the saved answer below.

Saved answer:
{saved_answer}

Format exactly:
### Front
A short recall question about the key physics law, formula, constant, figure, graph feature, or principle.

### Back
- Key idea:
- Formula / law / constant / figure:
- When to use it:
- Common trap:

Keep it compact and exam-focused. If no numeric constant or fixed figure applies, write "No fixed constant or figure".
""".strip()


def canonical_question_cache_key(base_root: str, image_path: str, fallback_key: str) -> str:
    try:
        base_abs = os.path.abspath(base_root)
        image_abs = os.path.abspath(image_path)
        common = os.path.commonpath([base_abs, image_abs])
        if common != base_abs:
            return fallback_key
        rel_path = os.path.relpath(image_abs, base_abs)
    except Exception:
        return fallback_key

    rel_parts = rel_path.split(os.sep)
    if len(rel_parts) < 4 or rel_path.startswith(".."):
        return fallback_key
    return rel_path.replace(os.sep, "/")


def question_type_course_for_cache_key(cache_key: str, fallback_course: str) -> str:
    first_part = (cache_key or "").split("/", 1)[0]
    if re.match(r"^M\d+\.", first_part or ""):
        return first_part
    return fallback_course
