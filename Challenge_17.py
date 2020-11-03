"""
This is a Python Program to reverse a given number.

Problem Description
The program takes a number and reverses it.

Problem Solution
1. Take the value of the integer and store in a variable.
2. Using a while loop, get each digit of the number and store the reversed number in another variable.
3. Print the reverse of the number.
4. Exit.
"""


from typing import Counter


def reverse_values():
    print()
    user_input = input("Enter any value to get it reversed: ")
    user_list = []
    for each_element in user_input:
        user_list.append(each_element)
    print("Moving it a list: ", user_list)
    reversed_number = user_input[::-1]
    print("Changing order: ", reversed_number)


def reverse_number():
    print()
    user_input = int(input("Enter any number to get it reversed: "))
    reversed_value = 0
    while (user_input > 0):
        dig = user_input % 10
        reversed_value = reversed_value * 10 + dig
        user_input = user_input//10
    print("Provided number is now been reversed and it's value: ", reversed_value)


reverse_number()
reverse_values()
