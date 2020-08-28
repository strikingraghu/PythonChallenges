"""
Problem Description
The program takes in a number and finds the sum of digits in a number.

Problem Solution
1. Take the value of the integer and store in a variable.
2. Using a while loop, get each digit of the number and add the digits to a variable.
3. Print the sum of the digits of the number.
4. Exit.
"""


def finding_total():
    print()

    get_num = input("Please enter a number having minimum 4 to 5 digits: ")
    temp_list = []
    for each_digit in get_num:
        temp_list.append(each_digit)
    print(temp_list)

    if len(temp_list) <= 3:
        print("Please enter a number having more than 4 digits")
    else:
        print("Thanks for providing a number!")

    total_value = 0
    for each_integer in temp_list:
        integer_value = int(each_integer)
        total_value = total_value + integer_value
    print("Thanks, total value of all integers provided in an input: ", total_value)


# calling function
finding_total()
