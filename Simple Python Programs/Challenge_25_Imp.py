"""
This is a Python Program to print prime numbers in a range using Sieve of Eratosthenes.

Problem Description
The program takes a range and prints prime numbers in that range using Sieve of Eratosthenes.

Problem Solution
1. Take the value of n from the user.
2. Initialise the sieve with numbers from 2 to n.
3. Use a while loop with the condition that the sieve is not empty
4. Get the smallest number that is prime
5. Remove that number and it’s multiples
6. Continue till the sieve is empty
7. Exit
"""


def fetch_sieve_eratosthenes():
    print()
    user_input = int(input("Enter any number of your choice: "))
    sieve = set(range(2, user_input+1))
    while sieve:
        prime = min(sieve)
        print(prime, end="\t")
        sieve -= set(range(prime, user_input+1, prime))
    print()


fetch_sieve_eratosthenes()
