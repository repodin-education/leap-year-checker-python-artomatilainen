# Leap Year Checker (Python)

# Task: Write a Python program that determines if a given year is a leap year.

def is_leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0:
            return False
        return True
    return False

# test
print(is_leap_year(2024))
print(is_leap_year(1900))
print(is_leap_year(2000))
