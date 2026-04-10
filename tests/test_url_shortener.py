"""Tests for URLShortener - User Story 1 (Basic URL Shortening)."""

import pytest
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import directly from the modules
from url_shortener import URLShortener


class TestUserStory1BasicURLShortening:
    """Test basic URL shortening functionality (User Story 1)."""
    
    def test_shorten_valid_url_returns_string_matching_pattern(self):
        """
        Test that shortening a valid URL returns a string.
        
        AC-1: Valid URL returns alphanumeric code
        """
        shortener = URLShortener()
        url = "https://example.com/very/long/url"
        
        code = shortener.shorten(url)
        
        assert isinstance(code, str)
        assert len(code) > 0
        # Should be Base62 alphanumeric
        assert code.isalnum()
    
    def test_resolve_existing_code_returns_original_url(self):
        """
        Test that resolving a short code returns the original URL.
        
        AC-3: Existing code resolves to correct URL
        """
        shortener = URLShortener()
        url = "https://example.com/very/long/url"
        
        code = shortener.shorten(url)
        resolved = shortener.resolve(code)
        
        assert resolved == url
    
    def test_resolve_is_case_sensitive(self):
        """
        Test that short codes are case-sensitive.
        
        Edge Case 6: resolve() is case-sensitive
        """
        shortener = URLShortener()
        
        # Find a code with at least one alphabetic character
        code = None
        url = None
        for i in range(200):
            candidate_url = f"https://example.com/{i}"
            candidate_code = shortener.shorten(candidate_url)
            if any(ch.isalpha() for ch in candidate_code):
                code = candidate_code
                url = candidate_url
                break
        assert code is not None, "Could not find a code with alphabetic characters in 200 attempts"
        
        # Same case should work
        assert shortener.resolve(code) == url
        
        # Case-swapped version should not work (case-sensitive)
        assert shortener.resolve(code.swapcase()) is None


class TestUserStory2ErrorHandling:
    """Test error handling and validation (User Story 2)."""
    
    def test_shorten_missing_protocol_raises_error(self):
        """
        Test that shortening URL without protocol raises ValueError.
        
        AC-5: Invalid URL raises ValueError
        """
        shortener = URLShortener()
        
        with pytest.raises(ValueError, match="http"):
            shortener.shorten("www.example.com")
    
    def test_shorten_empty_string_raises_error(self):
        """
        Test that shortening empty string raises ValueError.
        
        AC-5: Empty string raises ValueError
        """
        shortener = URLShortener()
        
        with pytest.raises(ValueError, match="empty"):
            shortener.shorten("")
    
    def test_resolve_non_existing_code_returns_none(self):
        """
        Test that resolving non-existent code returns None.
        
        AC-4: Non-existent code returns None
        """
        shortener = URLShortener()
        
        result = shortener.resolve("nonexistent")
        
        assert result is None


class TestUserStory3EdgeCases:
    """Test edge cases (User Story 3)."""
    
    def test_shorten_url_with_special_chars_preserves_them(self):
        """
        Test that URLs with special characters are preserved exactly.
        
        Edge Case 5: Special characters preserved
        """
        shortener = URLShortener()
        url = "https://example.com/path?query=value&other=data"
        
        code = shortener.shorten(url)
        resolved = shortener.resolve(code)
        
        assert resolved == url
    
    def test_shorten_same_url_returns_same_code(self):
        """
        Test idempotency - same URL returns same code.
        
        AC-2: Duplicate URL returns same code
        """
        shortener = URLShortener()
        url = "https://example.com/test"
        
        code1 = shortener.shorten(url)
        code2 = shortener.shorten(url)
        
        assert code1 == code2
