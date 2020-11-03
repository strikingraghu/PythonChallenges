"""
This is a Python Program to print all numbers in a range divisible by a given number.

Problem Description
The program prints all numbers in a range divisible by a given number.

Problem Solution
1. Take in the upper range and lower range limit from the user.
2. Take in the number to be divided by from the user.
3. Using a for loop, print all the factors which is divisible by the number.
4. Exit.
"""


def fetch_divisible_range():
    print()
    user_input_low_limit = int(input("Enter the starting range for this code: "))
    user_input_high_limit = int(input("Enter the ending range for this code: "))
    user_input_divisible_number = int(input("Enter the number to be used for divisible activities: "))

    divisible_list = []
    non_divisible_list = []
    building_range = range(user_input_low_limit, user_input_high_limit+1)
    for each_val in building_range:
        if each_val % user_input_divisible_number == 0:
            divisible_list.append(each_val)
        else:
            non_divisible_list.append(each_val)

    print("List of values that are divisible within the range: ", divisible_list)
    print("List of values that are not divisible within the range: ", non_divisible_list)


fetch_divisible_range()
