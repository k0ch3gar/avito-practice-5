"""In-memory URL shortener using Base62 encoding."""

from typing import Optional

from .base62 import encode_base62
from .url_validator import validate_url


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
            A short code (Base62 encoded)
            
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
        raise NotImplementedError
    
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
        raise NotImplementedError
