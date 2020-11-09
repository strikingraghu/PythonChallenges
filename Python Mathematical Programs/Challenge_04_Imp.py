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
                print("%d is a Prime Factor of a given number %d" %(i, get_specific_number))
        i = i + 1


fetch_prime_factors()
