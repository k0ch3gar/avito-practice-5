# URL Shortener Constitution

## Core Principles

### I. Test-First Development (NON-NEGOTIABLE)

TDD is mandatory for all features. The development cycle MUST follow this order:
1. Write a failing test that describes the desired behavior
2. Get user approval on the test specification
3. Implement the minimum code to make the test pass
4. Refactor as needed while keeping tests green

Red-Green-Refactor cycle MUST be strictly enforced. No production code without a failing test first.

### II. Library-First Architecture

Every feature starts as a standalone library. Libraries MUST be:
- Self-contained with clear, single responsibility
- Independently testable without external dependencies
- Fully documented with docstrings and type hints

No organizational-only libraries. Each library must justify its existence through clear purpose.

### III. Pure Business Logic

Business logic MUST be implemented without infrastructure concerns:
- No web frameworks, HTTP layers, or API endpoints in core libraries
- No database dependencies in business logic - use in-memory structures for state
- Clear separation between pure logic and side effects
- Technology choices MUST serve the domain, not the other way around

### IV. Input Validation & Contract Testing

All public APIs MUST validate inputs rigorously:
- Reject invalid inputs with descriptive ValueError or TypeError
- Validate URL format: require http:// or https:// protocols
- Reject empty strings, None values, and malformed data
- Test contract boundaries with edge cases

Integration tests MUST verify: new library contracts, contract changes, inter-service communication, shared schemas.

### V. Simplicity & YAGNI

Start simple and resist over-engineering:
- Implement only what is explicitly required
- Defer optional features until actually needed
- Reject speculative abstractions and "future-proofing"
- Prefer working solutions over theoretically optimal ones

## Technical Stack

- **Language**: Python (version from project initialization)
- **Testing**: pytest for unit and contract tests
- **Storage**: In-memory dict structures only (no databases)
- **Structure**: Single library at repository root (`src/` or direct)
- **Format**: Type hints required on all public interfaces

## Quality Standards

- All public methods MUST have docstrings explaining behavior
- All acceptance criteria from specifications MUST have corresponding tests
- Edge cases MUST be documented and tested
- Code MUST be self-documenting through clear naming

## Governance

This constitution supersedes all other development practices. Amendments require:
1. Documentation of the proposed change
2. Team approval through consensus
3. Migration plan for existing code if breaking

All PRs and reviews MUST verify compliance with these principles. Complexity MUST be justified - simpler alternatives rejected only with documented reasoning.

**Version**: 1.0.0 | **Ratified**: 2026-04-09 | **Last Amended**: 2026-04-09
