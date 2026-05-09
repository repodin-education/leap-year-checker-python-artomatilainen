
# AI Feedback: Leap Year Checker (Python)

**Overall Score:** 70/100 (Good)

---

## Summary

The student has successfully implemented the core logic for determining if a year is a leap year, demonstrating a solid understanding of conditional statements and modulo operations. The `is_leap_year` function correctly applies the rules, including handling century years. However, the submission falls short on the program's overall requirements, specifically regarding reading user input and formatting the output exactly as specified. Input validation is also not present.

---

## Strengths

- The core leap year logic is correctly implemented and handles all specified rules, including century year exceptions.
- The use of a dedicated function `is_leap_year` promotes modularity and reusability.
- Variable and function names are clear and descriptive, contributing to good readability.
- The inclusion of manual test cases within the `if __name__ == "__main__":` block is a good practice for self-verification.
- There is no input validation to handle non-integer inputs.
- Some inline comments are redundant, simply restating the code.
- The nested `if` structure for the leap year logic, while correct, can be simplified for conciseness.

---

## Improvement Areas

- The program does not read input from the user as required by the assignment. — Modify the main execution block to prompt the user for a year using `year = int(input("Enter a year: "))`.
- The output format does not match the exact requirements ('Leap year' or 'Not a leap year'). — Adjust the `print` statement to output the exact strings. For example, `print("Leap year")` if `is_leap_year` returns `True`, and `print("Not a leap year")` otherwise.
- There is no input validation to handle non-integer inputs. — Once you implement user input, wrap the `int(input())` call in a `try-except` block to catch `ValueError` if the user enters non-numeric data, and provide a user-friendly error message.
- Some inline comments are redundant, simply restating the code. — Focus comments on explaining the purpose or reasoning behind a particular block of code, or to clarify complex logic, rather than describing obvious operations. For example, instead of `# Check if divisible by 4`, you might explain the order of checks.
- The nested `if` structure for the leap year logic, while correct, can be simplified for conciseness. — Consider refactoring the `is_leap_year` function using a single `return` statement with logical operators (`and`, `or`) to express the conditions more compactly, such as `return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)`.
- The program does not read input from the user as required by the assignment.
- The output format does not match the exact requirements ('Leap year' or 'Not a leap year').
- There is no input validation to handle non-integer inputs.
- Some inline comments are redundant, simply restating the code.
- The nested `if` structure for the leap year logic, while correct, can be simplified for conciseness.

---

## Immediate Next Steps

- The program does not read input from the user as required by the assignment.: Modify the main execution block to prompt the user for a year using `year = int(input("Enter a year: "))`.
- The output format does not match the exact requirements ('Leap year' or 'Not a leap year').: Adjust the `print` statement to output the exact strings. For example, `print("Leap year")` if `is_leap_year` returns `True`, and `print("Not a leap year")` otherwise.
- There is no input validation to handle non-integer inputs.: Once you implement user input, wrap the `int(input())` call in a `try-except` block to catch `ValueError` if the user enters non-numeric data, and provide a user-friendly error message.
- Some inline comments are redundant, simply restating the code.: Focus comments on explaining the purpose or reasoning behind a particular block of code, or to clarify complex logic, rather than describing obvious operations. For example, instead of `# Check if divisible by 4`, you might explain the order of checks.
- The nested `if` structure for the leap year logic, while correct, can be simplified for conciseness.: Consider refactoring the `is_leap_year` function using a single `return` statement with logical operators (`and`, `or`) to express the conditions more compactly, such as `return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)`.

---

## Longer-Term Focus

- Modify the main execution block to prompt the user for a year using `year = int(input("Enter a year: "))`.
- Adjust the `print` statement to output the exact strings. For example, `print("Leap year")` if `is_leap_year` returns `True`, and `print("Not a leap year")` otherwise.
- Once you implement user input, wrap the `int(input())` call in a `try-except` block to catch `ValueError` if the user enters non-numeric data, and provide a user-friendly error message.
- Focus comments on explaining the purpose or reasoning behind a particular block of code, or to clarify complex logic, rather than describing obvious operations. For example, instead of `# Check if divisible by 4`, you might explain the order of checks.
- Consider refactoring the `is_leap_year` function using a single `return` statement with logical operators (`and`, `or`) to express the conditions more compactly, such as `return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)`.

---

*Generated by RepodIn AI*
**Student:** Arto Matilainen · **Repository:** `leap-year-checker-python-artomatilainen`
**Course:** Python · **Assignment:** Leap Year Checker (Python)
**Model:** RepodIn AI · **Generated:** May 9, 2026, 5:33 PM
