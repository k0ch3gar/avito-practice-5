"""Tests for URLShortener - User Story 1 (Basic URL Shortening)."""

import pytest
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

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
        url = "https://example.com"
        
        code = shortener.shorten(url)
        
        # Same case should work
        assert shortener.resolve(code) == url
        
        # Uppercase version should not work (case-sensitive)
        upper_code = code.upper()
        if upper_code != code:
            assert shortener.resolve(upper_code) is None
