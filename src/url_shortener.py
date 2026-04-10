"""In-memory URL shortener using Base62 encoding."""

from typing import Optional

try:
    from .base62 import encode_base62
    from .url_validator import validate_url
except ImportError:
    # When running directly or as __main__
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from base62 import encode_base62
    from url_validator import validate_url


class URLShortener:
    """In-memory URL shortener using Base62 encoding."""
    
    def __init__(self) -> None:
        """
        Initialize empty storage with counter at 0.
        
        Postcondition: _storage is empty, _counter is 0
        """
        self._storage: dict[str, str] = {}      # short_code -> original_url
        self._counter: int = 0                   # Auto-increment for codes
        self._url_to_code: dict[str, str] = {}     # original_url -> short_code (for idempotency)
    
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
        # Type check
        if not isinstance(original_url, str):
            raise TypeError("URL must be a string")
        
        # Validate URL
        is_valid, error_msg = validate_url(original_url)
        if not is_valid:
            raise ValueError(error_msg)
        
        # Strip URL for storage
        stripped_url = original_url.strip()
        
        # Check for idempotency - return existing code if URL exists
        if stripped_url in self._url_to_code:
            return self._url_to_code[stripped_url]
        
        # Generate new short code (6-8 Base62 characters, variable length)
        code = encode_base62(self._counter)
        
        # Store mappings (bi-directional)
        self._storage[code] = stripped_url
        self._url_to_code[stripped_url] = code
        
        # Increment counter
        self._counter += 1
        
        return code
    
    def resolve(self, short_code: str) -> Optional[str]:
        """
        Resolve a short code to its original URL.
        
        Args:
            short_code: A short code previously returned by shorten()
            
        Returns:
            The original URL if found, None otherwise
            
        Raises:
            TypeError: If short_code is not a string
            ValueError: If short_code is not at most 8 Base62 characters
        """
        # Type check
        if not isinstance(short_code, str):
            raise TypeError("Short code must be a string")
        
        # Validate short code format (max 8 Base62 characters)
        if len(short_code) > 8:
            raise ValueError("Short code must be at most 8 characters")
        
        # Check that all characters are valid Base62
        base62_chars = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if not all(c in base62_chars for c in short_code):
            raise ValueError("Short code must contain only Base62 characters (0-9, a-z, A-Z)")
        
        # Look up and return
        return self._storage.get(short_code)
