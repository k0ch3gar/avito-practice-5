"""Base62 encoding utilities."""

BASE62_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE62_LENGTH = len(BASE62_CHARS)  # 62


def encode_base62(value: int) -> str:
    """
    Encode a non-negative integer to a Base62 string.
    
    Args:
        value: Non-negative integer to encode.
        
    Returns:
        Base62 encoded string.
        
    Raises:
        ValueError: If value is negative.
    """
    if value < 0:
        raise ValueError("Value must be non-negative")
    
    if value == 0:
        return BASE62_CHARS[0]
    
    result = []
    while value > 0:
        value, remainder = divmod(value, BASE62_LENGTH)
        result.append(BASE62_CHARS[remainder])
    
    # Reverse to get most significant digit first
    return ''.join(reversed(result))


def decode_base62(encoded: str) -> int:
    """
    Decode a Base62 string to an integer.
    
    Args:
        encoded: Base62 encoded string.
        
    Returns:
        Decoded integer value.
        
    Raises:
        ValueError: If the string contains invalid characters.
    """
    result = 0
    for char in encoded:
        if char not in BASE62_CHARS:
            raise ValueError(f"Invalid Base62 character: {char}")
        result = result * BASE62_LENGTH + BASE62_CHARS.index(char)
    return result
