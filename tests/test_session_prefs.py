import os
import tempfile
import unittest

from src.session_prefs import SESSION_PREF_KEYS, load_session_prefs, save_session_prefs


class SessionPrefsTests(unittest.TestCase):
    def test_save_session_prefs_keeps_only_ui_state_keys(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "ui_session.json")
            save_session_prefs(
                path,
                {
                    "practice_mode": "Topic by Topic",
                    "course_level": "M7.The nature of light",
                    "selected_topic": "12.Light and special relativity",
                    "selected_subtopic": "12.2.Evidence for special relativity",
                    "question_index": 25,
                    "login_pass": "secret",
                },
            )

            loaded = load_session_prefs(path)

            self.assertEqual(loaded["practice_mode"], "Topic by Topic")
            self.assertEqual(loaded["question_index"], 25)
            self.assertNotIn("login_pass", loaded)
            self.assertTrue(set(loaded).issubset(SESSION_PREF_KEYS))

    def test_load_session_prefs_returns_empty_for_missing_or_invalid_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(load_session_prefs(os.path.join(tmp, "missing.json")), {})


if __name__ == "__main__":
    unittest.main()
