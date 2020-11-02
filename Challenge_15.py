"""
This is a Python Program to Calculate the Average of Numbers in a Given List.

Problem Description
The program takes the elements of the list one by one and displays the average of the elements of the list.

Problem Solution
1. Take the number of elements to be stored in the list as input.
2. Use a for loop to input elements into the list.
3. Calculate the total sum of elements in the list.
4. Divide the sum by total number of elements in the list.
5. Exit.
"""


def calculate_average():
    print()
    user_input = [int(x) for x in input("Enter few numbers: ").split()]
    input_list = []

    for each_element in user_input:
        input_list.append(each_element)
    print("Length of element in declared list: ", len(input_list))

    total_sum_value = 0
    for each_value in input_list:
        total_sum_value = total_sum_value + each_value
    print("Total sum of all element in declared list: ", total_sum_value)

    average_value = total_sum_value // len(input_list)
    print("Average value of all numbers being entered as an input: ", average_value)


calculate_average()
