"""
This is a Python Program to count the number of digits in a number.

Problem Description
The program takes the number and prints the number of digits in the number.

Problem Solution
1. Take the value of the integer and store in a variable.
2. Using a while loop, get each digit of the number and increment the count each time a digit is obtained.
3. Print the number of digits in the given integer.
4. Exit.
"""


def fetch_numbers_length():
    print()
    user_input = input("Please provide a longest number: ")
    user_input_list = []
    total_count = 0
    for each_num in user_input:
        int_value = int(each_num)
        user_input_list.append(int_value)
        total_count = total_count + 1
    print(user_input_list)
    print("Total number of integers in provided input: ", total_count)


def fetch_integers_length():
    print()
    user_input = int(input("Enter any lengthy number of your choice: "))
    total_count = 0
    while user_input > 0:
        user_input = user_input // 10
        total_count = total_count + 1
    print("Total number of integers in provided input: ", total_count)


fetch_numbers_length()
fetch_integers_length()
