import unittest

from src.auth_approval import (
    ROOT_USER,
    apply_approval_policy,
    can_generate_shared_answer_from_submission,
    is_root_user,
    is_user_approved,
    llm_owner_username,
)


class AuthApprovalTests(unittest.TestCase):
    def test_root_user_is_case_insensitive(self):
        self.assertTrue(is_root_user("StephenQU72@GMAIL.COM"))
        self.assertEqual(ROOT_USER, "stephenqu72@gmail.com")

    def test_apply_approval_policy_approves_root_and_pends_existing_users(self):
        db = {
            "users": {
                "stephenqu72@gmail.com": {"salt": "a", "hash": "b"},
                "student@example.com": {"salt": "c", "hash": "d"},
            }
        }

        updated, changed = apply_approval_policy(db)

        self.assertTrue(changed)
        self.assertTrue(updated["users"]["stephenqu72@gmail.com"]["approved"])
        self.assertEqual(updated["users"]["stephenqu72@gmail.com"]["role"], "root")
        self.assertFalse(updated["users"]["student@example.com"]["approved"])
        self.assertEqual(updated["users"]["student@example.com"]["role"], "user")

    def test_apply_approval_policy_keeps_approved_users_approved(self):
        db = {"users": {"student@example.com": {"salt": "c", "hash": "d", "approved": True, "role": "user"}}}

        updated, changed = apply_approval_policy(db)

        self.assertFalse(changed)
        self.assertTrue(updated["users"]["student@example.com"]["approved"])

    def test_is_user_approved_allows_root_even_without_record(self):
        self.assertTrue(is_user_approved("stephenqu72@gmail.com", None))
        self.assertFalse(is_user_approved("student@example.com", {"approved": False}))
        self.assertTrue(is_user_approved("student@example.com", {"approved": True}))

    def test_llm_owner_username_is_always_root(self):
        self.assertEqual(llm_owner_username("student@example.com"), ROOT_USER)
        self.assertEqual(llm_owner_username("stephenqu72@gmail.com"), ROOT_USER)

    def test_submitted_answers_can_generate_shared_teacher_answer(self):
        self.assertTrue(can_generate_shared_answer_from_submission("student@example.com"))
        self.assertTrue(can_generate_shared_answer_from_submission("stephenqu72@gmail.com"))


if __name__ == "__main__":
    unittest.main()
