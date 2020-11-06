"""
This is a Python Program to read two numbers and print their quotient and remainder.

Problem Description
The program takes two numbers and prints the quotient and remainder.

Problem Solution
1. Take in the first and second number and store it in separate variables.
2. Then obtain the quotient using division and the remainder using modulus operator.
3. Exit.
"""


def get_quotient_remainder():
    print()
    user_input = input("Enter any 2 numbers: ").split()
    first_val = user_input[0]
    second_val = user_input[1]
    
    get_quotient = int(first_val) // int(second_val)
    get_remainder = int(first_val) % int(second_val)
    print("Quotient:", get_quotient, "&", "Remainder:", get_remainder)


get_quotient_remainder()
