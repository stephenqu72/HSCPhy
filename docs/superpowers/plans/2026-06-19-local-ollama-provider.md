# Local Ollama Gemma 4 Provider Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a localhost Ollama `gemma4:26b` provider that supports every existing LLM workflow without changing saved-answer formats or Gemini behavior.

**Architecture:** Create a focused `src/llm_provider.py` module that normalizes Gemini and Ollama calls into a response object exposing `.text`. Keep provider selection and user-specific Gemini key setup in `app.py`, but route all text and image generation through the new module. Ollama uses the standard-library HTTP client and sends PNG images as base64 to `/api/chat`.

**Tech Stack:** Python 3.11, Streamlit, Pillow, Google Generative AI SDK, Ollama native HTTP API, `unittest`.

---

### Task 1: Provider Detection And Ollama Request Construction

**Files:**
- Create: `src/llm_provider.py`
- Create: `tests/test_llm_provider.py`

- [ ] **Step 1: Write failing provider tests**

Add tests proving that `is_ollama_model("ollama:gemma4:26b")` is true, Gemini names remain false, text prompts produce a `/api/chat` JSON request, PIL images are encoded into the message `images` list, and successful JSON is normalized to `LLMResponse.text`.

- [ ] **Step 2: Run the focused test and verify RED**

Run: `python -m unittest tests.test_llm_provider -v`

Expected: FAIL because `src.llm_provider` does not exist.

- [ ] **Step 3: Implement the minimal provider module**

Create:

```python
@dataclass(frozen=True)
class LLMResponse:
    text: str

OLLAMA_MODEL_PREFIX = "ollama:"

def is_ollama_model(model_name: str) -> bool: ...
def display_model_name(model_name: str) -> str: ...
def call_ollama(prompt, image=None, host=None, model=None, timeout=300, opener=None) -> LLMResponse: ...
def call_llm(prompt, image, selected_model, gemini_factory, configure_gemini, ollama_host=None, ollama_model=None) -> LLMResponse: ...
```

Use `urllib.request.Request` and `urlopen`. The payload is `{"model": model, "messages": [{"role": "user", "content": prompt}], "stream": false}`; add a PNG base64 string under `images` when an image is supplied.

- [ ] **Step 4: Run the focused test and verify GREEN**

Run: `python -m unittest tests.test_llm_provider -v`

Expected: all provider construction tests PASS.

### Task 2: Ollama Failures And Gemini Regression

**Files:**
- Modify: `src/llm_provider.py`
- Modify: `tests/test_llm_provider.py`

- [ ] **Step 1: Write failing error and routing tests**

Add tests for connection refusal, HTTP 404 missing model, invalid JSON, missing `message.content`, empty content, and Gemini routing through the supplied factory/configuration callback.

- [ ] **Step 2: Run the focused test and verify RED**

Run: `python -m unittest tests.test_llm_provider -v`

Expected: new tests FAIL with unhandled transport/response errors.

- [ ] **Step 3: Add clear provider exceptions**

Implement `LLMProviderError` and translate failures into messages that say either:

```text
Unable to connect to local Ollama at http://localhost:11434. Start Ollama and try again.
```

or:

```text
Ollama model gemma4:26b is unavailable. Run: ollama pull gemma4:26b
```

Reject malformed and empty responses before returning. Preserve Gemini `.text` behavior through `LLMResponse` normalization.

- [ ] **Step 4: Run the focused test and verify GREEN**

Run: `python -m unittest tests.test_llm_provider -v`

Expected: all provider tests PASS.

### Task 3: Route Every App Workflow Through The Provider

**Files:**
- Modify: `app.py`
- Modify: `tests/test_llm_provider.py`

- [ ] **Step 1: Write a failing selector/routing contract test**

Add a test proving the public selector value `ollama:gemma4:26b` maps to display label `Local Ollama - gemma4:26b`, and that Ollama routing does not invoke Gemini configuration.

- [ ] **Step 2: Run the focused test and verify RED**

Run: `python -m unittest tests.test_llm_provider -v`

Expected: FAIL until the display contract and routing behavior exist.

- [ ] **Step 3: Integrate the provider in `app.py`**

Import the provider helpers. Add `ollama:gemma4:26b` to `model_options` using a `format_func` label. Change `call_model` and `call_text_model` to call `call_llm`. Replace the direct Gemini chat construction with `call_model(user_input, image)`. Keep all answer, classification, feedback, video, flash-card, graph, and bulk workflows on these shared functions.

Only call `configure_gemini_for_current_user()` at startup when the selected/default provider is Gemini; Ollama selection must be able to run without Gemini keys. Preserve the existing selected model session state and default Gemini option.

- [ ] **Step 4: Run provider and existing unit tests**

Run: `python -m unittest discover -s tests -p "test_*.py" -v`

Expected: all tests PASS.

### Task 4: Configuration And End-To-End Verification

**Files:**
- Modify: `.env.example` only if it exists
- Verify: `app.py`, `src/llm_provider.py`, `tests/test_llm_provider.py`

- [ ] **Step 1: Verify syntax**

Run: `python -m compileall app.py src tests`

Expected: compilation succeeds with no syntax errors.

- [ ] **Step 2: Verify no direct feature-level Gemini calls remain**

Run: `rg -n "GenerativeModel|generate_content" app.py`

Expected: Gemini SDK construction exists only inside the shared provider adapter callback, with no separate chat or feature-specific calls.

- [ ] **Step 3: Verify local Ollama availability without changing the app**

Run: `ollama list`

Expected: `gemma4:26b` appears. If Ollama is not installed or the model is absent, report the exact setup command without treating it as a code failure.

- [ ] **Step 4: Run the full test suite again**

Run: `python -m unittest discover -s tests -p "test_*.py"`

Expected: all tests PASS.

- [ ] **Step 5: Review the final diff**

Run: `git diff -- app.py src/llm_provider.py tests/test_llm_provider.py`

Expected: changes are limited to provider abstraction, selector integration, and tests; user `.env`, `.streamlit`, `persist`, and cache files remain untouched.
