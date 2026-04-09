# Quickstart: URL Shortener Library

## Installation

```bash
# Clone the repository
git clone <repo-url>
cd <repo-name>

# Install dependencies (pytest for testing)
pip install pytest
```

## Basic Usage

```python
from src.url_shortener import URLShortener

# Create instance
shortener = URLShortener()

# Shorten a URL
code = shortener.shorten("https://example.com/very/long/url")
print(f"Short code: {code}")  # e.g., "aB3x9Z"

# Resolve back to original
original = shortener.resolve(code)
print(f"Original: {original}")  # https://example.com/very/long/url
```

## Complete Example

```python
from src.url_shortener import URLShortener

# Initialize
shortener = URLShortener()

# Shorten URLs
code1 = shortener.shorten("https://google.com/search?q=python")
code2 = shortener.shorten("https://github.com/user/repo")

# Resolve
print(shortener.resolve(code1))  # https://google.com/search?q=python
print(shortener.resolve(code2))  # https://github.com/user/repo

# Idempotency - same URL returns same code
code1_again = shortener.shorten("https://google.com/search?q=python")
assert code1 == code1_again  # Same code returned

# Non-existent code
result = shortener.resolve("nonexistent")
print(result)  # None
```

## Testing

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/unit/test_url_shortener.py -v

# Run with coverage
pytest tests/ --cov=src --cov-report=term-missing
```

## Project Structure

```
.
├── src/
│   └── url_shortener.py    # Main library
├── tests/
│   ├── unit/
│   │   └── test_url_shortener.py
│   └── contract/
│       └── test_contracts.py
└── pyproject.toml
```

## API Reference

### `URLShortener`

| Method | Signature | Description |
|--------|-----------|-------------|
| `__init__` | `() -> None` | Initialize empty storage |
| `shorten` | `(original_url: str) -> str` | Shorten URL, return code |
| `resolve` | `(short_code: str) -> str \| None` | Resolve code to URL |

### Errors

```python
# Invalid URL raises ValueError
shortener.shorten("not-a-url")      # ValueError: Invalid URL format
shortener.shorten("www.example.com") # ValueError: Missing protocol
shortener.shorten("")               # ValueError: Empty URL
shortener.shorten(None)             # TypeError
```
