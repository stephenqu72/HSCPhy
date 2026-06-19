import unittest

from src.gemini_keys import GeminiKeySelection
from src.gemini_requests import GeminiRequestError, generate_with_gemini


class GeminiRequestTests(unittest.TestCase):
    def test_successful_response_passes_through(self):
        expected_response = object()

        class FakeModel:
            def generate_content(self, content):
                self.content = content
                return expected_response

        response = generate_with_gemini(
            GeminiKeySelection("GEMINI_API_KEY_2", "secret-value"),
            "gemini-test",
            ["prompt", "image"],
            model_factory=lambda model_name: FakeModel(),
        )

        self.assertIs(response, expected_response)

    def test_failure_includes_alias_and_redacts_secret_value(self):
        class FakeModel:
            def generate_content(self, content):
                raise RuntimeError("403 leaked key secret-value")

        with self.assertRaises(GeminiRequestError) as raised:
            generate_with_gemini(
                GeminiKeySelection("GEMINI_API_KEY_2", "secret-value"),
                "gemini-test",
                "prompt",
                model_factory=lambda model_name: FakeModel(),
            )

        message = str(raised.exception)
        self.assertIn("GEMINI_API_KEY_2", message)
        self.assertIn("403 leaked key", message)
        self.assertNotIn("secret-value", message)
        self.assertIsNone(raised.exception.__cause__)


if __name__ == "__main__":
    unittest.main()
