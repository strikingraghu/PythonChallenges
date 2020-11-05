"""
This is a Python Program to read a number n and print the natural numbers summation pattern.

Problem Description
The program takes a number n and prints the natural numbers summation pattern.

Problem Solution
1. Take a value from the user and store it in a variable n.
2. Use two for loop where the value of j ranges between the values of 1 and n and value of i ranges between 1 and j.
3. Print the value of i and ‘+’ operator while appending the value of i to a list.
4. Then find the sum of elements in the list.
5. Print ‘=’ followed by the total sum.
6. Exit.
"""


def natural_number_summation():
    print()
    n = int(input("Enter a number: "))
    for j in range(1, n + 1):
        a = []
        for i in range(1, j + 1):
            print(i, sep=" ", end=" ")
            if i < j:
                print("+", sep=" ", end=" ")
            a.append(i)
        print("=", sum(a))


natural_number_summation()
