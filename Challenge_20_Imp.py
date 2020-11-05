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

"""
This is a Python Program to read a number n and print an identity matrix of the desired size.

Problem Description
The program takes a number n and prints an identity matrix of the desired size.

Problem Solution
1. Take a value from the user and store it in a variable n.
2. Use two for loop where the value of j ranges between the values of 0 and n-1 
3. Value of i also ranges between 0 and n-1.
4. Print the value of 1 when i is equal to j and 0 otherwise.
5. Exit.
"""


def fetch_possible_combinations():
    print()
    first_input = int(input("Enter 1st number: "))
    second_input = int(input("Enter 2nd number: "))
    third_input = int(input("Enter 3rd number: "))
    values_list = [first_input, second_input, third_input]
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                if i != j & j != k & k != i:
                    print(values_list[i], values_list[j], values_list[k])


def build_identity_matrix():
    print()
    user_input = int(input("Enter any number of your choice: "))
    for i in range(0, user_input):
        for j in range(0, user_input):
            if i == j:
                print("1", sep=" ", end=" ")
            else:
                print("0", sep=" ", end=" ")
        print()


# fetch_possible_combinations()
build_identity_matrix()
