import os
import tempfile
import unittest

from src.student_answers import (
    append_answer_log,
    build_answer_feedback_prompt,
    build_flash_card_prompt,
    build_answer_summary,
    canonical_question_cache_key,
    latest_answers_by_key,
    parse_flash_card,
    question_type_course_for_cache_key,
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
            {
                "key": "q1",
                "answer": "A",
                "question_type": "Multiple choice",
                "timestamp": "2026-01-01T00:00:00Z",
                "feedback": "Correct choice.",
            },
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
        self.assertEqual(summary["rows"][0]["Feedback"], "Correct choice.")
        self.assertNotIn("three.png", [row["Image"] for row in summary["rows"]])

    def test_build_answer_feedback_prompt_contains_both_answers(self):
        prompt = build_answer_feedback_prompt(
            "Multiple choice",
            "B",
            "The correct answer is B because the wave speed is constant.",
        )

        self.assertIn("Question type: Multiple choice", prompt)
        self.assertIn("Student answer:\nB", prompt)
        self.assertIn("Saved teacher answer:\nThe correct answer is B", prompt)
        self.assertIn("Give concise, encouraging feedback", prompt)

    def test_build_flash_card_prompt_uses_saved_answer_for_exam_facts(self):
        prompt = build_flash_card_prompt("Use F = ma and gravitational acceleration g = 9.8 m s^-2.")

        self.assertIn("saved answer", prompt.lower())
        self.assertIn("key physics law", prompt)
        self.assertIn("formula", prompt.lower())
        self.assertIn("constant", prompt.lower())
        self.assertIn("figure", prompt.lower())
        self.assertIn("Use F = ma", prompt)

    def test_parse_flash_card_splits_front_and_back(self):
        flash_card = parse_flash_card(
            """
### Front
What does Newton's second law connect?

### Back
- Key idea: Force causes acceleration
- Formula / law / constant / figure: F = ma
""".strip()
        )

        self.assertEqual(flash_card["front"], "What does Newton's second law connect?")
        self.assertIn("F = ma", flash_card["back"])

    def test_canonical_question_cache_key_matches_topic_by_topic_key(self):
        with tempfile.TemporaryDirectory() as tmp:
            image_path = os.path.join(
                tmp,
                "M7.The nature of light",
                "9.Exploring the Electromagnetic Spectrum",
                "9.1.Electromagnetism",
                "Barker 2020 Y12_Picture 43.png",
            )
            fallback_key = "Physics/PastPaper/Barker_2020_Y12/M7.The nature of light/9.Exploring the Electromagnetic Spectrum/9.1.Electromagnetism/Barker 2020 Y12_Picture 43.png"

            cache_key = canonical_question_cache_key(tmp, image_path, fallback_key)

            self.assertEqual(
                cache_key,
                "M7.The nature of light/9.Exploring the Electromagnetic Spectrum/9.1.Electromagnetism/Barker 2020 Y12_Picture 43.png",
            )

    def test_canonical_question_cache_key_uses_fallback_outside_base_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            fallback_key = "Physics/PastPaper/paper/question.png"

            cache_key = canonical_question_cache_key(tmp, os.path.join(os.path.dirname(tmp), "question.png"), fallback_key)

            self.assertEqual(cache_key, fallback_key)

    def test_question_type_course_for_cache_key_uses_module_prefix(self):
        cache_key = "M7.The nature of light/12.Light and special relativity/12.2.Evidence/image.png"

        course = question_type_course_for_cache_key(cache_key, "Physics")

        self.assertEqual(course, "M7.The nature of light")

    def test_question_type_course_for_cache_key_uses_fallback_for_past_paper_key(self):
        cache_key = "Physics/PastPaper/Barker_2020/image.png"

        course = question_type_course_for_cache_key(cache_key, "Physics")

        self.assertEqual(course, "Physics")


if __name__ == "__main__":
    unittest.main()
