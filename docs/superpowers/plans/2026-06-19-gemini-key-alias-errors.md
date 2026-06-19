# Gemini Key Alias Errors Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Show the selected Gemini key alias when a Gemini request fails, without exposing the key value.

**Architecture:** Add a focused request helper that accepts a `GeminiKeySelection`, invokes the configured model, and wraps exceptions with the alias after redacting the secret value. Route image, text, and chat requests through this helper.

**Tech Stack:** Python 3.11, Google Generative AI SDK, Streamlit, `unittest`.

---

### Task 1: Add Safe Gemini Request Error Context

**Files:**
- Create: `src/gemini_requests.py`
- Create: `tests/test_gemini_requests.py`

- [ ] Write tests proving successful responses pass through and failures contain `GEMINI_API_KEY_2` but never the actual secret.
- [ ] Run the focused test and confirm it fails because the helper does not exist.
- [ ] Implement `generate_with_gemini(selection, model_name, content, model_factory)` and a `GeminiRequestError` exception.
- [ ] Run the focused test and confirm it passes.

### Task 2: Route App Requests Through The Helper

**Files:**
- Modify: `app.py`

- [ ] Import the request helper.
- [ ] Update `call_model` and `call_text_model` to retain the selected key result and call the helper.
- [ ] Replace the direct chat Gemini request with `call_model`.
- [ ] Verify no feature-level `generate_content` calls remain outside the helper.
- [ ] Run all tests, syntax compilation, and diff checks.
- [ ] Commit only the helper, tests, and app integration.
