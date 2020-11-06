"""
This is a Python Program to find the smallest divisor of an integer.

Problem Description
The program takes in an integer and prints the smallest divisor of the integer.

Problem Solution
1. Take in an integer from the user.
2. Use a for loop where the value of i ranges from 2 to the integer.
3. If the number is divisible by i, the value of i is appended to the list.
4. The list is then sorted and the smallest element is printed.
5. Exit.
"""


def fetch_smallest_divisor():
    print()

    user_input = int(input("Enter any number of your choice: "))
    assumed_range = range(2, user_input+1)
    print("Range decided for running this script: ", assumed_range)
    assumed_list = []
    for each_integer in assumed_range:
        if user_input % each_integer == 0:
            assumed_list.append(each_integer)
    assumed_list.sort()
    print("Picking the smallest divisor for a given number: ", assumed_list[0])


fetch_smallest_divisor()
