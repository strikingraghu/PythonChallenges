"""
This is a Python Program to check whether a given number is a palindrome.

Problem Description
The program takes a number and checks whether it is a palindrome or not.

Problem Solution
1. Take the value of the integer and store in a variable.
2. Transfer the value of the integer into another temporary variable.
3. Using a while loop, get each digit of the number and store the reversed number in another variable.
4. Check if the reverse of the number is equal to the one in the temporary variable.
5. Print the final result.
6. Exit.
"""


def evaluate_palindrome_pattern():
    print()
    user_input = input("Enter any number of you choice: ")
    user_list = []
    for each_number in user_input:
        each_integer = int(each_number)
        user_list.append(each_integer)
    reversed_list = user_list[::-1]
    if user_list == reversed_list:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")


def check_palindrome_pattern():
    print()
    user_input = int(input("Enter any number of you choice: "))
    temp_var1 = user_input
    temp_var2 = 0
    while user_input > 0:
        dig = user_input % 10
        temp_var2 = temp_var2 * 10 + dig
        user_input = user_input // 10
    if temp_var1 == temp_var2:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")


evaluate_palindrome_pattern()
check_palindrome_pattern()
