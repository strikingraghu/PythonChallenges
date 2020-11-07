"""
This is a Python Program to compute simple interest given all the required values.

Problem Description
The program computes simple interest given the principle amount, rate and time.

Problem Solution
1. Take in the values for principle amount, rate and time.
2. Using the formula, compute the simple interest.
3. Print the value for the computed interest.
4. Exit.
"""


def calculate_interest():
    print()

    try:
        base_amount = int(input("Enter the total amount borrowed: "))
        base_interest = int(input("Enter the interest rate applicable: "))
        base_years = int(input("Enter the number of years to repay: "))
        calculate_overall_interest = base_amount * base_interest // 100 * base_years
        print("Overall interest to be paid for", base_years, "years is", calculate_overall_interest)
    except ValueError:
        print("ValueError:: Please provide integers only!")


"""
This is a Python Program to check whether a given year is a leap year or not.

Problem Description
The program takes in a year and checks whether it is a leap year or not.

Problem Solution
1. Take the value of the year as input
2. Using an if-statement, check whether the year is a leap year or not
3. Print the final result
4. Exit
"""


def validate_leap_year():
    print()

    try:
        year = int(input("Enter a specific year of your choice: "))
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print("Wow, it's a leap year!")
        else:
            print("Entered year is not a leap year, try again!")
    except ValueError as ve:
        print(ve.__traceback__)
        print("ValueError: Please provide integers value only!")


calculate_interest()
validate_leap_year()
