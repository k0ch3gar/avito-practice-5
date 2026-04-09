# API Contract: URLShortener

## Interface

```python
from typing import Optional

class URLShortener:
    """In-memory URL shortener."""
    
    def __init__(self) -> None:
        """
        Initialize empty storage.
        Postcondition: _storage is empty, _counter is 0
        """
        ...
    
    def shorten(self, original_url: str) -> str:
        """
        Shorten a URL and store the mapping.
        
        Args:
            original_url: A valid URL string with http:// or https:// protocol
            
        Returns:
            A short code (6-8 Base62 characters)
            
        Raises:
            ValueError: If URL is invalid (missing protocol, empty, etc.)
            TypeError: If URL is not a string
            
        Preconditions:
            - original_url must be a string
            - original_url must start with http:// or https://
            - original_url must not be empty after stripping
            
        Postconditions:
            - Mapping exists in storage for returned code
            - resolve(code) returns original_url
        """
        ...
    
    def resolve(self, short_code: str) -> Optional[str]:
        """
        Resolve a short code to its original URL.
        
        Args:
            short_code: A short code previously returned by shorten()
            
        Returns:
            The original URL if found, None otherwise
            
        Raises:
            TypeError: If short_code is not a string
        """
        ...
```

## Contract Invariants

1. **Storage Consistency**: For every entry in `_storage`, the reverse mapping exists in `_url_to_code`
2. **Counter Monotonicity**: `_counter` never decreases
3. **Idempotency**: Calling `shorten(url)` twice with same URL returns same code
4. **No Data Loss**: URLs are stored and retrieved exactly as provided

## Base62 Encoding Contract

- Character set: `0-9`, `a-z`, `A-Z` (62 characters)
- Encoding: Pure integer-to-string conversion of counter value
- Output length: Variable, typically 1-6 characters for reasonable counter ranges

## Error Handling Contract

| Input | Behavior |
|-------|----------|
| `shorten(None)` | `TypeError` |
| `shorten("")` | `ValueError` |
| `shorten("  ")` | `ValueError` |
| `shorten("www.example.com")` | `ValueError` (missing protocol) |
| `shorten("ftp://example.com")` | `ValueError` (unsupported protocol) |
| `shorten("https://example.com")` | Success, returns code |
| `resolve(None)` | `TypeError` |
| `resolve("")` | Returns `None` |
| `resolve("nonexistent")` | Returns `None` |
| `resolve("valid_code")` | Returns URL or `None` if not found |
