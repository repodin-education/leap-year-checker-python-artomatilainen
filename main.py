"""
Comprehensive test suite for the leap year checker.

This module uses pytest for testing. Run with:
    pytest test_leap_year.py -v

Or with Python's unittest:
    python -m unittest test_leap_year.py
"""

import pytest
from leap_year import is_leap_year


class TestBasicLeapYearRules:
    """Test the basic divisible-by-4 rule."""

    def test_regular_leap_year(self):
        """Years divisible by 4 should be leap years."""
        assert is_leap_year(2024) is True
        assert is_leap_year(2020) is True
        assert is_leap_year(2016) is True

    def test_regular_non_leap_year(self):
        """Years not divisible by 4 should not be leap years."""
        assert is_leap_year(2023) is False
        assert is_leap_year(2022) is False
        assert is_leap_year(2021) is False
        assert is_leap_year(2019) is False


class TestCenturyYearExceptions:
    """Test the century year exceptions (divisible by 100)."""

    def test_century_non_leap_years(self):
        """Century years not divisible by 400 should not be leap years."""
        assert is_leap_year(1900) is False
        assert is_leap_year(1800) is False
        assert is_leap_year(1700) is False
        assert is_leap_year(2100) is False

    def test_century_leap_years(self):
        """Century years divisible by 400 should be leap years."""
        assert is_leap_year(2000) is True
        assert is_leap_year(1600) is True
        assert is_leap_year(2400) is True


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_year_zero(self):
        """Year 0 should be handled (divisible by 400)."""
        assert is_leap_year(0) is True

    def test_early_years(self):
        """Test some early historical years."""
        assert is_leap_year(4) is True
        assert is_leap_year(8) is True
        assert is_leap_year(100) is False
        assert is_leap_year(400) is True

    def test_recent_years(self):
        """Test years around current time."""
        assert is_leap_year(2020) is True
        assert is_leap_year(2021) is False
        assert is_leap_year(2022) is False
        assert is_leap_year(2023) is False
        assert is_leap_year(2024) is True


class TestInputValidation:
    """Test input validation and error handling."""

    def test_invalid_type_string(self):
        """Should raise TypeError for string input."""
        with pytest.raises(TypeError):
            is_leap_year("2024")

    def test_invalid_type_float(self):
        """Should raise TypeError for float input."""
        with pytest.raises(TypeError):
            is_leap_year(2024.5)

    def test_invalid_type_none(self):
        """Should raise TypeError for None input."""
        with pytest.raises(TypeError):
            is_leap_year(None)

    def test_negative_year(self):
        """Should raise ValueError for negative years."""
        with pytest.raises(ValueError):
            is_leap_year(-1)
        with pytest.raises(ValueError):
            is_leap_year(-2024)


class TestComprehensiveCoverage:
    """Comprehensive test cases covering all rule combinations."""

    @pytest.mark.parametrize("year,expected", [
        # Basic divisible by 4
        (4, True), (8, True), (12, True), (2024, True),
        # Not divisible by 4
        (1, False), (2, False), (3, False), (2023, False),
        # Century years (divisible by 100 but not 400)
        (100, False), (200, False), (300, False), (1900, False),
        # Quadricentennial years (divisible by 400)
        (400, True), (800, True), (1200, True), (2000, True),
        # Mixed cases
        (1896, True), (1897, False), (1898, False), (1899, False),
        (1996, True), (1997, False), (1998, False), (1999, False),
        (2096, True), (2097, False), (2098, False), (2099, False),
        (2100, False), (2104, True),
    ])
    def test_parametrized_years(self, year, expected):
        """Test multiple years with parametrized testing."""
        assert is_leap_year(year) is expected


# Run tests if executed directly
if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
