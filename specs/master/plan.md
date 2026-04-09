# Implementation Plan: In-Memory URL Shortener

**Branch**: `master` | **Date**: 2026-04-09 | **Spec**: [link](../spec.md)

## Summary

Build a Python library `URLShortener` that shortens URLs using Base62-encoded auto-increment counter with in-memory dict storage. Pure business logic with no web layer, following TDD methodology.

## Technical Context

**Language/Version**: Python 3.x  
**Primary Dependencies**: pytest (testing only)  
**Storage**: In-memory `dict` (short_code -> original_url)  
**Testing**: pytest  
**Target Platform**: Cross-platform (pure Python)  
**Project Type**: Library (pure business logic)  
**Performance Goals**: O(1) for shorten/resolve operations  
**Constraints**: Synchronous single-threaded only  
**Scale/Scope**: Single instance, session-bound storage  

## Constitution Check

| Gate | Status | Notes |
|------|--------|-------|
| TDD mandatory | ✅ PASS | Tests will be written first per spec requirements |
| Library-first | ✅ PASS | Pure Python library, no web frameworks |
| Pure business logic | ✅ PASS | No infrastructure concerns, dict only |
| Input validation | ✅ PASS | URL validation with http://https:// requirement |
| Simplicity/YAGNI | ✅ PASS | Only explicitly required features |

## Project Structure

### Documentation (this feature)

```text
specs/master/
├── plan.md              # This file
├── research.md          # N/A - no unknowns to resolve
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (API contract)
└── tasks.md             # Phase 2 output (/speckit.tasks - NOT created here)
```

### Source Code (repository root)

```text
src/
└── url_shortener.py     # URLShortener class

tests/
├── unit/
│   └── test_url_shortener.py  # Unit tests
└── contract/
    └── test_contracts.py      # Contract tests

pyproject.toml           # Project config with pytest
```

**Structure Decision**: Simple single-library structure. `URLShortener` class in `src/url_shortener.py`, tests in `tests/` with unit and contract subdirectories.

## Complexity Tracking

No violations to justify.

## Phase 0: Research

No unknowns identified. All technical details are specified in the feature spec:
- Python chosen as implementation language
- Base62 encoding with auto-increment counter specified
- In-memory dict storage explicitly required
- pytest for testing mandated

## Phase 1: Design & Contracts

### Data Model

**Entity: URLShortener**

| Field | Type | Description |
|-------|------|-------------|
| `_storage` | `dict[str, str]` | Mapping short_code -> original_url |
| `_counter` | `int` | Auto-incrementing counter for code generation |
| `_url_to_code` | `dict[str, str]` | Reverse mapping for idempotency |

### Interface Contract

**Public API:**

```python
class URLShortener:
    def __init__(self) -> None:
        """Initialize in-memory storage."""
    
    def shorten(self, original_url: str) -> str:
        """
        Validate URL, generate short code, store mapping.
        Returns: 6-8 character Base62 code
        Raises: ValueError for invalid URLs
        """
    
    def resolve(self, short_code: str) -> str | None:
        """
        Look up original URL by short code.
        Returns: Original URL or None if not found
        """
```

### Acceptance Criteria Mapping

| AC | Test Scenario |
|----|---------------|
| AC-1 | Valid URL returns 6-8 char alphanumeric code, resolve returns original |
| AC-2 | Duplicate URL returns same code (idempotency) |
| AC-3 | Existing code resolves to correct URL |
| AC-4 | Non-existent code returns None |
| AC-5 | Invalid URL raises ValueError |

### Edge Cases to Test

1. URL without protocol (www.google.com) -> ValueError
2. Empty string / None input -> ValueError/TypeError
3. Whitespace handling (.strip() and internal spaces)
4. Very long URLs (2000+ chars)
5. URLs with special characters preserved exactly
