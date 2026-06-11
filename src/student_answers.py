import json
import os


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
            }
        )
    return {
        "answered_count": len(rows),
        "total_count": len(selection),
        "rows": rows,
    }
