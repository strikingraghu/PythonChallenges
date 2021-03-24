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

import fractions


def fetch_integer_divisible_multiple():
    print()
    user_input_start_range = int(input("Enter the starting range value for this program: "))
    user_input_end_range = int(input("Enter the ending range value for this program: "))
    building_range = range(user_input_start_range, user_input_end_range + 1)
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
        print("Value Error: ", ve)


perform_perfect_number_validation()

"""
This is a Python Program to check if a number is a strong number.

Problem Description
The program takes a number and checks if it is a strong number.

Problem Solution
1. Take in an integer and store it in a variable.
2. Using two while loops, find the factorial of each of the digits in the number.
3. Then sum up all the factorials of the digits.
4. Check if the sum of the factorials of the digits is equal to the number.
5. Print the final result.
6. Exit.
"""


def perform_strong_number_validation():
    print()
    user_number = int(input("Enter any number of your choice for Strong number identification: "))
    sum_val = 0
    temp_val = user_number
    while temp_val > 0:
        factorial = 1
        iteration_val = 1
        reminder = temp_val % 10

        while iteration_val <= reminder:
            factorial = factorial * iteration_val
            iteration_val = iteration_val + 1

        print("\n Factorial of %d = %d" % (reminder, factorial))
        sum_val = sum_val + factorial
        temp_val = temp_val // 10

    print("\n Sum of Factorials of a given number %d = %d" % (user_number, sum_val))

    if sum_val == user_number:
        print("%d is a Strong number" % user_number)
    else:
        print("%d is not a Strong number" % user_number)


perform_strong_number_validation()

"""
This is a Python Program to find the LCM of two numbers.

Problem Description
The program takes two numbers and prints the LCM of two numbers.

Problem Solution
1. Take in both the integers and store it in separate variables.
2. Find which of the integer among the two is smaller and store it in a separate variable.
3. Use a while loop whose condition is always True until break is used.
4. Use an if statement to check if both the numbers are divisible by the minimum number and increment otherwise.
5. Print the final LCM.
6. Exit.

Program Explanation
1. User must enter both the numbers and store it in separate variables.
2. An if statement is used to find out which of the numbers is smaller and store in a minimum variable.
3. Then a while loop is used whose condition is always true (or 1) unless break is used.
4. Then an if statement within the loop is used to check whether the value in the minimum variable is divisible by both the numbers.
5. If it is divisible, break statement breaks out of the loop.
6. If it is not divisible, the value in the minimum variable is incremented.
7. The final LCM is printed.
"""


def finding_lcm_value():
    first_val = int(input("Enter the first number of your choice for LCM value: "))
    second_val = int(input("Enter the first number of your choice for LCM value: "))

    if first_val > second_val:
        min1 = first_val
    else:
        min1 = second_val
    
    while(1):
        if (min1 % first_val == 0 and min1 % second_val == 0):
            print("LCM is: ", min1)
            break
        min1 = min1 + 1


finding_lcm_value()

"""
Problem Description
The program takes two numbers and prints the GCD of two numbers.

Problem Solution
1. Import the fractions module.
2. Take in both the integers and store it in separate variables.
3. Use the in-built function to find the GCD of both the numbers.
4. Print the GCD.
5. Exit.
"""


def finding_gcd_value():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    print("The GCD of the two numbers is",fractions.gcd(a,b))


finding_gcd_value()
