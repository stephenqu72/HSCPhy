import unittest

from src.usernames import normalize_user_db, normalize_username


class UsernameTests(unittest.TestCase):
    def test_normalize_username_trims_and_lowercases(self):
        self.assertEqual(normalize_username("  StephenQU72@GMAIL.COM  "), "stephenqu72@gmail.com")

    def test_normalize_user_db_lowercases_existing_account_keys(self):
        db = {
            "users": {
                "StephenQU72@GMAIL.COM": {"salt": "a", "hash": "b"},
                "other@example.com": {"salt": "c", "hash": "d"},
            }
        }

        normalized, changed = normalize_user_db(db)

        self.assertTrue(changed)
        self.assertIn("stephenqu72@gmail.com", normalized["users"])
        self.assertNotIn("StephenQU72@GMAIL.COM", normalized["users"])
        self.assertEqual(normalized["users"]["other@example.com"]["salt"], "c")

    def test_normalize_user_db_keeps_existing_lowercase_duplicate(self):
        db = {
            "users": {
                "USER@example.com": {"salt": "old", "hash": "old"},
                "user@example.com": {"salt": "new", "hash": "new"},
            }
        }

        normalized, changed = normalize_user_db(db)

        self.assertTrue(changed)
        self.assertEqual(normalized["users"]["user@example.com"]["salt"], "new")


if __name__ == "__main__":
    unittest.main()
