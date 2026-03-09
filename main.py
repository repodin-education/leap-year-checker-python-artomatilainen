"""
Leap year checker module 9th of Mars, 2026. Testing #4
"""

def is_leap_year(year):
    """Check if a year is a leap year"""
    # Check if divisible by 4
    if year % 4 == 0:
        # Check century years
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


# Manual testing
if __name__ == "__main__":
    test_years = [2024, 2023, 1900, 2000, 2400]
    for year in test_years:
        result = is_leap_year(year)
        print(f"{year}: {result}")
