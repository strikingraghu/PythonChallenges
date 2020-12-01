"""
This is a Python Program to find those numbers which are divisible by 7 and multiple of 5 in a given range of numbers.

Problem Description
The program takes an upper range and lower range and finds those numbers within the range which are divisible by 7 and multiple of 5.

Problem Solution
1. Take in the upper and lower range and store it in separate variables.
2. Use a for loop which ranges from the lower range to the upper range.
3. Then find the numbers which are divisible by both 5 and 7.
4. Print those numbers
5. Exit.
"""


def fetch_integer_divisible_multiple():
    print()
    user_input_start_range = int(input("Enter the starting range value for this program: "))
    user_input_end_range = int(input("Enter the ending range value for this program: "))
    building_range = range(user_input_start_range, user_input_end_range+1)
    for each_int in building_range:
        if each_int % 7 == 0 and each_int % 5 == 0:
            print(each_int, "= divisble by 7 and it's a multiple of 5")


fetch_integer_divisible_multiple()
