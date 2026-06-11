import os
import tempfile
import unittest

from src.student_answers import (
    append_answer_log,
    build_answer_summary,
    latest_answers_by_key,
    read_json_list,
)


class StudentAnswerTests(unittest.TestCase):
    def test_append_and_latest_answer_by_key(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "answers.json")
            append_answer_log(path, {"key": "q1", "answer": "first", "timestamp": "2026-01-01T00:00:00Z"})
            append_answer_log(path, {"key": "q1", "answer": "second", "timestamp": "2026-01-02T00:00:00Z"})
            append_answer_log(path, {"key": "q2", "answer": "A", "timestamp": "2026-01-01T12:00:00Z"})

            self.assertEqual(len(read_json_list(path)), 3)
            latest = latest_answers_by_key(read_json_list(path))

            self.assertEqual(latest["q1"]["answer"], "second")
            self.assertEqual(latest["q2"]["answer"], "A")

    def test_build_answer_summary_filters_to_current_selection(self):
        entries = [
            {"key": "q1", "answer": "A", "question_type": "Multiple choice", "timestamp": "2026-01-01T00:00:00Z"},
            {"key": "q2", "answer": "worked response", "question_type": "Short answer", "timestamp": "2026-01-02T00:00:00Z"},
            {"key": "outside", "answer": "ignore me", "question_type": "Essay", "timestamp": "2026-01-03T00:00:00Z"},
        ]
        selection = [
            {"key": "q1", "image": "one.png", "question_type": "Multiple choice"},
            {"key": "q2", "image": "two.png", "question_type": "Short answer"},
            {"key": "q3", "image": "three.png", "question_type": "Other questions"},
        ]

        summary = build_answer_summary(entries, selection)

        self.assertEqual(summary["answered_count"], 2)
        self.assertEqual(summary["total_count"], 3)
        self.assertEqual([row["Question"] for row in summary["rows"]], [1, 2])
        self.assertEqual(summary["rows"][0]["Answer"], "A")
        self.assertNotIn("three.png", [row["Image"] for row in summary["rows"]])


if __name__ == "__main__":
    unittest.main()
