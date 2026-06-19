# Gemini Key Alias Error Design

Date: 2026-06-19

## Goal

Identify the configured Gemini key alias responsible for a failed request without exposing the API key value.

## Design

Add a small Gemini request wrapper that first obtains the `GeminiKeySelection` from `configure_gemini_for_current_user()`, executes the model request, and re-raises failures with the selected `key_name` included. The message format is:

```text
Gemini request failed using GEMINI_API_KEY_2: <provider error>
```

Only aliases from the configured key-name list are included. API key values are never included in the exception, UI, or logs by this code.

Both image and text generation helpers will use the wrapper. The question chat path will be routed through the image helper, covering answers, regeneration, classification, feedback, chat, video help, flash cards, and bulk generation.

## Testing

Unit tests will verify that failed calls include the selected alias, exclude the secret value, and preserve successful response behavior.
