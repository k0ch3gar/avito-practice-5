# Data Model: URL Shortener

## Entity: URLShortener

### Class Structure

```python
from typing import Optional

class URLShortener:
    """In-memory URL shortener using Base62 encoding."""
    
    def __init__(self) -> None:
        """Initialize empty storage with counter at 0."""
        self._storage: dict[str, str] = {}      # short_code -> original_url
        self._counter: int = 0                   # Auto-increment for codes
        self._url_to_code: dict[str, str] = {}   # original_url -> short_code (for idempotency)
```

### Field Details

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `_storage` | `dict[str, str]` | Keys: 6-8 Base62 chars | Primary mapping storage |
| `_counter` | `int` | >= 0 | Monotonically increasing |
| `_url_to_code` | `dict[str, str]` | Keys: valid URLs | Reverse index for idempotency |

### Relationships

- `_storage` and `_url_to_code` are synchronized (bi-directional mapping)
- `_counter` determines next code, incremented after each `shorten()` call

### State Transitions

```
URLShortener instance lifecycle:
  __init__() -> empty state (empty dicts, counter=0)
       |
       v
  shorten(url) -> adds to _storage, _url_to_code; increments _counter
       |
       v
  resolve(code) -> reads from _storage (read-only)
       |
       v
  (instance destruction) -> storage lost (in-memory only)
```

### Validation Rules

1. **URL Validation** (in `shorten()`):
   - Must start with `http://` or `https://`
   - Reject empty strings, None
   - Strip whitespace, reject if internal whitespace remains

2. **Short Code Validation** (in `resolve()`):
   - Must be non-empty string
   - Should be 6-8 Base62 characters (enforced by generation, not storage)

### Code Generation Algorithm

Base62 encoding of counter value:
- Characters: `0-9`, `a-z`, `A-Z` (62 total)
- Counter 0 → "0", Counter 1 → "1", ... Counter 9 → "9"
- Counter 10 → "a", Counter 36 → "A"
- Minimum code length: 6 characters (padded with leading zeros or shortest representation)

### Idempotency

When `shorten()` is called with a URL that already exists in `_url_to_code`:
- Return the existing short code (no new entry created)
- Counter is NOT incremented
- This is AC-2 requirement
