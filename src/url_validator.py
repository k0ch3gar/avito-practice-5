"""URL validation utilities."""

from typing import Optional


def validate_url(url: str) -> tuple[bool, Optional[str]]:
    """
    Validate a URL string.
    
    Args:
        url: The URL string to validate.
        
    Returns:
        A tuple of (is_valid, error_message).
        If valid, error_message is None.
        
    Rules:
        - Must be a string
        - Must start with http:// or https://
        - Must not be empty after stripping
        - Must not contain internal whitespace
    """
    if not isinstance(url, str):
        return False, "URL must be a string"
    
    # Normalize URL (strip whitespace)
    normalized_url = url.strip()
    
    if not normalized_url:
        return False, "URL cannot be empty"
    
    # Check for internal whitespace (any whitespace character)
    if any(ch.isspace() for ch in normalized_url):
        return False, "URL cannot contain internal whitespace"
    
    # Check protocol
    if not (url.startswith('http://') or url.startswith('https://')):
        return False, "URL must start with http:// or https://"
    
    return True, None


def is_valid_url(url: str) -> bool:
    """Return True if URL is valid, False otherwise."""
    is_valid, _ = validate_url(url)
    return is_valid
