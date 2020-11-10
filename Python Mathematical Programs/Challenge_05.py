"""
This is a Python Program to print the table of a given number.

Problem Description
The program takes in a number and prints the table of a given number.

Problem Solution
1. Take in a number and store it in a variable.
2. Print the multiplication tables of a given number.
3. Exit.
"""


def create_tables_output():
    print()
    try:
        user_input = int(input("Enter a number of your choice to build multiplication tables: "))
        for each_int in range(1, 11):
            print(user_input, "x", each_int, "=", user_input * each_int)
    except ValueError as ve:
        print("ValueError: Provide integers only!")


create_tables_output()
