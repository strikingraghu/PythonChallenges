"""
This is a Python Program to generate all the divisors of an integer.

Problem Description
The program takes a number and generates all the divisors of the number.

Problem Solution
1. Take the value of the integer and store it in a variable.
2. Use a for loop and if statement to generate the divisors of the integer.
3. Print the divisors of the number.
4. Exit.
"""


def get_integer_divisors():
    print()
    try:
        user_input = int(input("Enter any number if your choice: "))
        setting_range = range(2, user_input + 1)
        for each_range_value in setting_range:
            if user_input % each_range_value == 0:
                print(each_range_value)
    except ValueError as ve:
        print("Please provide a number in the input section!")
        print(ve.__doc__)


get_integer_divisors()

"""
This is a Python Program to compute prime factors of an integer.

Problem Description
The program takes a number and computes the prime factors of the integer.

Problem Solution
1. Take the value of the integer and store in a variable.
2. Using a while loop, first obtain the factors of the number.
3. Using another while loop within the previous one, compute if the factors are prime or not.
4. Exit.
"""


def fetch_prime_factors():
    print()
    get_specific_number = int(input("Enter any number of your choice: "))
    i = 1
    while i <= get_specific_number:
        count = 0
        if get_specific_number % i == 0:
            j = 1
            while j <= i:
                if i % j == 0:
                    count = count + 1
                j = j + 1

            if count == 2:
                print("%d is one of the prime factor for %d" % (i, get_specific_number))
        i = i + 1


fetch_prime_factors()
