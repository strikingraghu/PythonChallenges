"""
This is a Python Program to read a number n and compute n+nn+nnn.

Problem Description
The program takes a number n and computes n+nn+nnn.

Problem Solution
1. Take the value of a element and store in a variable n.
2. Convert the integer into string and store it in another variable.
3. Add the string twice so the string gets concatenated and store it in another variable.
4. Then add the string thrice and assign the value to the third variable.
5. Convert the strings in the second and third variables into integers.
6. Add the values in all the integers.
7. Print the total value of the expression.
8. Exit.
"""


def concatenate_get_sum():
    print()
    user_input = input("Enter the number of your choice: ")
    
    # value concatenation activities
    numerical_val = str(user_input)
    first_element = numerical_val
    second_element = numerical_val + numerical_val
    third_element = numerical_val + numerical_val + numerical_val
    print("Pattern generated for the provided value: ", first_element, second_element, third_element)

    # identify total value
    total_sum = int(first_element) + int(second_element) + int(third_element)
    print("Total value after concatenation: ", total_sum)


concatenate_get_sum()
