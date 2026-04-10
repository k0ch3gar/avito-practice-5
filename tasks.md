# Tasks: In-Memory URL Shortener

**Input**: Design documents from spec.md  
**Prerequisites**: spec.md (functional requirements and acceptance criteria)  
**Tests**: pytest tests required (TDD approach)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Project Initialization)

**Purpose**: Create project structure and initialize Python project

- [x] T001 Create project structure: `src/` and `tests/` directories
- [x] T002 Initialize Python project with pytest dependency (`pip install pytest`)
- [x] T003 [P] Configure pytest in `pytest.ini` or `pyproject.toml`

---

## Phase 2: Foundational (Core Components)

**Purpose**: Base URLShortener class with in-memory storage and Base62 encoder

- [x] T004 [P] Create URL validator utility in `src/url_validator.py`
- [x] T005 [P] Create Base62 encoder utility in `src/base62.py`
- [x] T006 Create main URLShortener class in `src/url_shortener.py` with:
  - `__init__()` method initializing in-memory `dict` storage
  - `shorten(original_url: str) -> str` method signature
  - `resolve(short_code: str) -> Optional[str]` method signature

---

## Phase 3: User Story 1 - URL Shortening (Priority: P1) 🎯 MVP

**Goal**: Shorten valid URLs and retrieve original URLs by short code

**Independent Test**: `pytest tests/test_url_shortener.py::TestUserStory1BasicURLShortening::test_shorten_valid_url_returns_string_matching_pattern`

### Tests for User Story 1 (TDD - write FIRST)

- [x] T007 [P] [US1] Test `test_shorten_valid_url_returns_string_matching_pattern` in `tests/test_url_shortener.py`
- [x] T008 [P] [US1] Test `test_resolve_existing_code_returns_original_url` in `tests/test_url_shortener.py`
- [x] T009 [P] [US1] Test `test_resolve_is_case_sensitive` in `tests/test_url_shortener.py`

### Implementation for User Story 1

- [x] T010 [US1] Implement `shorten()` method in `src/url_shortener.py`:
  - Validate URL with protocol (http:// or https://)
  - Check for idempotency (same URL → same code)
  - Generate unique Base62 code using counter
  - Store mapping in dict
- [x] T011 [US1] Implement `resolve()` method in `src/url_shortener.py`:
  - Look up short_code in dict
  - Return original URL or None if not found

**Checkpoint**: User Story 1 should pass all tests

---

## Phase 4: User Story 2 - URL Validation & Error Handling (Priority: P2)

**Goal**: Reject invalid URLs with appropriate exceptions

**Independent Test**: `pytest tests/test_url_shortener.py::TestUserStory2ErrorHandling::test_shorten_missing_protocol_raises_error`

### Tests for User Story 2 (TDD - write FIRST)

- [x] T012 [P] [US2] Test `test_shorten_missing_protocol_raises_error` in `tests/test_url_shortener.py`
- [x] T013 [P] [US2] Test `test_shorten_empty_string_raises_error` in `tests/test_url_shortener.py`
- [x] T014 [P] [US2] Test `test_resolve_non_existing_code_returns_none` in `tests/test_url_shortener.py`

### Implementation for User Story 2

- [x] T015 [US2] Update `shorten()` in `src/url_shortener.py`:
  - Raise `ValueError` for empty string
  - Raise `ValueError` for URLs without http:// or https://
  - Raise `TypeError` for non-string types
- [x] T016 [US2] Update `resolve()` in `src/url_shortener.py`:
  - Raise `TypeError` for non-string short_code

**Checkpoint**: User Story 2 should pass all tests

---

## Phase 5: User Story 3 - Edge Cases (Priority: P3)

**Goal**: Handle special characters, whitespace, and preserve URL integrity

**Independent Test**: `pytest tests/test_url_shortener.py::TestUserStory3EdgeCases::test_shorten_url_with_special_chars_preserves_them`

### Tests for User Story 3 (TDD - write FIRST)

- [x] T017 [P] [US3] Test `test_shorten_url_with_special_chars_preserves_them` in `tests/test_url_shortener.py`
- [x] T018 [P] [US3] Test handling of URLs with query parameters and anchors
- [x] T019 [P] [US3] Test handling of very long URLs (2000+ characters)

### Implementation for User Story 3

- [x] T020 [US3] Update URL validator in `src/url_validator.py`:
  - Strip whitespace from URL ends
  - Reject URLs with internal spaces
  - Preserve special characters in path/query/fragment
- [x] T021 [US3] Verify `shorten()` and `resolve()` preserve exact URL string

**Checkpoint**: User Story 3 should pass all tests

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final verification and documentation

- [x] T022 Run full test suite: `pytest tests/test_url_shortener.py -v`
- [x] T023 Verify all 8 required test names from spec pass
- [x] T024 Add module docstring to `src/url_shortener.py`

---

## Dependency Graph

```text
Phase 1 (Setup) ──────────────────────────────────────────────────────┐
                                                                    │
Phase 2 (Foundational) ─────────────────────────────────────────────┤
                                                                    │
Phase 3 (US1) ──────────────────────────────────────────────────────┤
  └──── Tests T007, T008, T009 can run in parallel                    │
  └──── Implementation T010 → T011 (depends on T006)                  │
                                                                    │
Phase 4 (US2) ───────────────────────────────────────────────────────┤
  └──── Tests T012, T013, T014 can run in parallel                    │
  └──── Implementation T015 → T016 (depends on T010, T011)            │
                                                                    │
Phase 5 (US3) ───────────────────────────────────────────────────────┤
  └──── Tests T017, T018, T019 can run in parallel                    │
  └──── Implementation T020 → T021 (depends on T015, T016)           │
                                                                    │
Phase 6 (Polish) ─────────────────────────────────────────────────────┘
```

---

## Parallel Execution Opportunities

| Phase | Parallel Tasks | Reason |
|-------|---------------|--------|
| Phase 1 | T001, T002, T003 | Project setup, no dependencies |
| Phase 2 | T004, T005 | Utility modules, independent of each other |
| Phase 3 | T007, T008, T009 | Tests for different test functions |
| Phase 4 | T012, T013, T014 | Tests for different test functions |
| Phase 5 | T017, T018, T019 | Tests for different test functions |

---

## Suggested MVP Scope

**User Story 1 only** (T007, T008, T009, T010, T011) — basic shorten and resolve functionality

---

## Summary

- **Total Tasks**: 24
- **User Story 1 (US1)**: 5 tasks (T007-T011)
- **User Story 2 (US2)**: 5 tasks (T012-T016)
- **User Story 3 (US3)**: 5 tasks (T017-T021)
- **Setup**: 3 tasks (T001-T003)
- **Foundational**: 3 tasks (T004-T006)
- **Polish**: 3 tasks (T022-T024)
- **Parallel Execution Groups**: 5 groups identified
- **MVP Scope**: User Story 1 (5 tasks)

---

## Required Test Names (from spec.md)

All tests must be implemented in `tests/test_url_shortener.py`:

1. `test_shorten_valid_url_returns_string_matching_pattern` (AC-1)
2. `test_shorten_same_url_returns_same_code` (AC-2, idempotency)
3. `test_resolve_existing_code_returns_original_url` (AC-3)
4. `test_resolve_non_existing_code_returns_none` (AC-4)
5. `test_shorten_missing_protocol_raises_error` (AC-5)
6. `test_shorten_empty_string_raises_error` (AC-5)
7. `test_shorten_url_with_special_chars_preserves_them` (Edge Case 5)
8. `test_resolve_is_case_sensitive` (Edge Case 6)

---

## Extension Hooks

No hooks registered in `.specify/extensions.yml` for this phase.
