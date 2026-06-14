import unittest

from src.password_reset import set_user_password


class PasswordResetTests(unittest.TestCase):
    def test_set_user_password_updates_salt_hash_and_timestamp(self):
        db = {"users": {"student@example.com": {"salt": "old", "hash": "oldhash", "approved": True}}}

        updated = set_user_password(
            db,
            "student@example.com",
            "new-password",
            salt_factory=lambda: "newsalt",
            hash_password=lambda password, salt: f"{password}:{salt}:hash",
            updated_at="2026-06-14T00:00:00Z",
        )

        user = updated["users"]["student@example.com"]
        self.assertEqual(user["salt"], "newsalt")
        self.assertEqual(user["hash"], "new-password:newsalt:hash")
        self.assertEqual(user["password_updated"], "2026-06-14T00:00:00Z")
        self.assertTrue(user["approved"])

    def test_set_user_password_normalizes_username(self):
        db = {"users": {"student@example.com": {"salt": "old", "hash": "oldhash"}}}

        updated = set_user_password(
            db,
            " Student@Example.COM ",
            "new-password",
            salt_factory=lambda: "s",
            hash_password=lambda password, salt: "h",
            updated_at="now",
        )

        self.assertEqual(updated["users"]["student@example.com"]["hash"], "h")

    def test_set_user_password_rejects_missing_user(self):
        with self.assertRaisesRegex(KeyError, "missing@example.com"):
            set_user_password(
                {"users": {}},
                "missing@example.com",
                "pw",
                salt_factory=lambda: "s",
                hash_password=lambda password, salt: "h",
                updated_at="now",
            )

    def test_set_user_password_rejects_blank_password(self):
        with self.assertRaisesRegex(ValueError, "Password cannot be blank"):
            set_user_password(
                {"users": {"student@example.com": {}}},
                "student@example.com",
                " ",
                salt_factory=lambda: "s",
                hash_password=lambda password, salt: "h",
                updated_at="now",
            )


if __name__ == "__main__":
    unittest.main()
