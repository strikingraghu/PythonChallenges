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
