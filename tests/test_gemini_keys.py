import unittest

from src.gemini_keys import select_gemini_key


class GeminiKeyTests(unittest.TestCase):
    def test_student_uses_student_key_on_any_weekday(self):
        keys = {
            "GEMINI_API_KEY": "root0",
            "GEMINI_API_KEY_1": "root1",
            "GEMINI_API_KEY_2": "root2",
            "GEMINI_API_KEY_stu": "student",
        }

        selected = select_gemini_key("student@example.com", keys, weekday_index=4)

        self.assertEqual(selected.key_name, "GEMINI_API_KEY_stu")
        self.assertEqual(selected.api_key, "student")

    def test_root_rotates_keys_by_weekday(self):
        keys = {
            "GEMINI_API_KEY": "root0",
            "GEMINI_API_KEY_1": "root1",
            "GEMINI_API_KEY_2": "root2",
            "GEMINI_API_KEY_stu": "student",
        }

        self.assertEqual(select_gemini_key("stephenqu72@gmail.com", keys, 0).key_name, "GEMINI_API_KEY")
        self.assertEqual(select_gemini_key("stephenqu72@gmail.com", keys, 1).key_name, "GEMINI_API_KEY_1")
        self.assertEqual(select_gemini_key("stephenqu72@gmail.com", keys, 2).key_name, "GEMINI_API_KEY_2")
        self.assertEqual(select_gemini_key("stephenqu72@gmail.com", keys, 3).key_name, "GEMINI_API_KEY")

    def test_missing_student_key_raises_clear_error(self):
        with self.assertRaisesRegex(ValueError, "GEMINI_API_KEY_stu"):
            select_gemini_key("student@example.com", {}, weekday_index=0)

    def test_missing_root_key_raises_clear_error(self):
        keys = {
            "GEMINI_API_KEY": "root0",
            "GEMINI_API_KEY_1": "root1",
            "GEMINI_API_KEY_stu": "student",
        }

        with self.assertRaisesRegex(ValueError, "GEMINI_API_KEY_2"):
            select_gemini_key("stephenqu72@gmail.com", keys, weekday_index=2)


if __name__ == "__main__":
    unittest.main()
