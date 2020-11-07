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


calculate_interest()
