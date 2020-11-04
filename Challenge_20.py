"""
This is a Python Program to accept three distinct digits and print all possible combinations from the digits.

Problem Description
The program takes three distinct numbers and prints all possible combinations from the digits.

Problem Solution
1. Take in the first, second and third number and store it in separate variables.
2. Then append all the three numbers to the list.
3. Use three for loops and print the digits in the list if none of their indexes are equal to each other.
4. Exit.
"""


def fetch_possible_combinations():
    print()
    first_input = int(input("Enter 1st number: "))
    second_input = int(input("Enter 2nd number: "))
    third_input = int(input("Enter 3rd number: "))
    values_list = []
    values_list.append(first_input)
    values_list.append(second_input)
    values_list.append(third_input)
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                if(i!=j & j!=k & k!=i):
                    print(values_list[i], values_list[j], values_list[k])


fetch_possible_combinations()
