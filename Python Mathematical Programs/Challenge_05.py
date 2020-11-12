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

"""
This is a Python Program to print the sum of negative numbers, positive even numbers and positive odd numbers in a given list.

Problem Description
The program prints the sum of negative numbers, positive even numbers and positive odd numbers in a given list..

Problem Solution
1. Take in the number of elements to be in the list from the user.
2. Take in the elements from the user using a for loop and append to a list.
3. Using a for loop, get the elements one by one from the list and check if it is positive or negative.
4. If it is positive, check if it is odd or even and find the individual sum.
5. Find the individual sum of negative numbers.
6. Print all the sums.
7. Exit.
"""


def calculate_various_pattern_numbers():
    print()
    try:
        input_loop_val = int(input("Enter the length of numbers you want to provide: "))
        setting_range = range(1, input_loop_val+1)
        for each_get_val in setting_range:
            print(each_get_val)
    except ValueError as ve:
        pass


calculate_various_pattern_numbers()
