"""
This is a Python Program to print all numbers in a range divisible by a given number.

Problem Description
The program prints all numbers in a range divisible by a given number.

Problem Solution
1. Take in the upper range and lower range limit from the user.
2. Take in the number to be divided by from the user.
3. Using a for loop, print all the factors which is divisible by the number.
4. Exit.
"""


def range_divisible_evaluation():
    print()

    user_values = input("Give 3 num, 1st number is for 'Divisible By' & remaining numbers for range: ").split()
    if len(user_values) == 3:
        print("Thanks for entering the required values")
    else:
        print("Sorry, please enter correct values again!")

    divisible_by = int(user_values[0])
    start_range_num = int(user_values[1])
    end_range_num = int(user_values[2])

    # building numbers within the range
    total_numbers = range(start_range_num, end_range_num)
    print("Numbers between the range: ", total_numbers)

    # evaluating divisible operations of numbers within the range
    divisible_list = []
    non_divisible_list = []
    for each_num in total_numbers:
        if each_num % divisible_by == 0:
            divisible_list.append(each_num)
        else:
            non_divisible_list.append(each_num)

    # final results
    print("Numbers that are divisible: ", divisible_list)
    print("Numbers that are not divisible: ", non_divisible_list)


# calling function
range_divisible_evaluation()
