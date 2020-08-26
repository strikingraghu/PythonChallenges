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


def calculating_average():
    print()

    incoming_values = [int(x) for x in input("Enter few numbers: ").split()]
    dynamic_list = []
    for each_incoming_element in incoming_values:
        dynamic_list.append(each_incoming_element)
    
    # calculate sum & average
    list_lenth = len(dynamic_list)
    total_sum = 0
    for each_element in dynamic_list:
        total_sum = total_sum + each_element
    print("Sum of all elements within the list: ", total_sum)
    print("Average value: ", total_sum/list_lenth)    


# calling function
calculating_average()

"""
This is a Python Program to exchange the values of two numbers without using a temporary variable.

Problem Description
The program takes both the values from the user and swaps them without using temporary variable.

Problem Solution
1. Take the values of both the elements from the user.
2. Store the values in separate variables.
3. Add both the variables and store it in the first variable.
4. Subtract the second variable from the first and store it in the second variable.
5. Then, subtract the first variable from the second variable and store it in the first variable.
6. Print the swapped values.
7. Exit.
"""


def swapping_values():
    print()

    incoming_values = input("Enter only 2 numbers to swap values: ").split()
    if len(incoming_values) >= 3:
        print("Enter only 2 values!")
    else:
        print("Thanks for entering only 2 values!")
    
    x = incoming_values[0]
    y = incoming_values[1]
    print("Values before swap :", x, "|", y)
    x, y = y, x
    print("Values after swap :", x, "|", y)


# calling function
swapping_values()
