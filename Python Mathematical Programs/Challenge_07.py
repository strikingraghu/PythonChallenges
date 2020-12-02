"""
Python Challenges
"""

"""
This is a Python Program to find those numbers which are divisible by 7 and multiple of 5 in a given range of numbers.

Problem Description
The program takes an upper range and lower range and finds those numbers that are divisible by 7 and multiple of 5.

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
            print(each_int, "= divisible by 7 and it's a multiple of 5")


fetch_integer_divisible_multiple()


"""
This is a Python Program to check if a number is an Armstrong number.

Problem Description
The program takes a number and checks if it is an Armstrong number.

Problem Solution
1. Take in an integer and store it in a variable.
2. Convert each digit of the number to a string variable and store it in a list.
3. Then cube each of the digits and store it in another list.
4. Find the sum of the cube of digits in the list and check if it is equal to the original number.
5. Print the final result.
6. Exit.
"""


def validate_armstrong_feature():
    print()

    total_sum = 0
    try:
        user_input = input("Enter any number of your choice: ")
        for each_digit in user_input:
            int_conversion_val = int(each_digit)
            cube_value = int_conversion_val ** 3
            total_sum = total_sum + cube_value
        print("Total sum of all integers calculated after raising it to power 3 for each digit: ", total_sum)

        if total_sum == int(user_input):
            print("So, number entered in an input matches with Armstrong criteria")
        else:
            print("Hence, number entered in an input doesn't matches with Armstrong criteria")
    except ValueError as ve:
        print("Value Error: ", ve)


validate_armstrong_feature()


"""
This is a Python Program to check if a number is a Perfect number.

Problem Description
The program takes a number and checks if it is a Perfect number.

Problem Solution
1. Take in an integer and store it in a variable.
2. Initialize a variable to count the sum of the proper divisors to 0.
3. Use a for loop and an if statement to add the proper divisors of the integer to the sum variable.
4. Check if the sum of the proper divisors of the number is equal to the variable.
5. Print the final result.
6. Exit.
"""


def perform_perfect_number_validation():
    print()
    try:
        user_input = input("Enter any number of your choice: ")
        total_sum = 0
        for each_digit in user_input:
            int_converted_val = int(each_digit)
            if int(user_input) % int_converted_val == 0:
                total_sum = total_sum + int_converted_val
        print("Completed looping activities")

        if total_sum == int(user_input):
            print("Wow, you entered a Perfect number!")
        else:
            print("Cool, try again to identify a Perfect number!")
    except ValueError as ve:
        print("Value Error: ", ve.__traceback__)


perform_perfect_number_validation()
