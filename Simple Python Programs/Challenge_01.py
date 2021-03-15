"""
Given a non-negative number represented as an array of digits, add 1 to the number.
(Increment the number represented by the digits)
The digits are stored such that the most significant digit is at the head of the list.
Example:
If the array has [4, 5, 6] the resultant array should be [4, 5, 7] as 456 + 1 = 457.
Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases are:
    The first line of each test case contains a single integer N denoting the size of array.
    The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.
Output:
Print the space separated resultant array in a separate line for each case.
Input:
    2
    4
    5 6 7 8
    3
    9 9 9
Output:
    5 6 7 9
    1 0 0 0
"""


def increment_array_element():
    print()
    incoming_values = input("Enter few digits: ").split()

    #  converting input values to int type
    values_list = []
    for each_element in incoming_values:
        change_type = int(each_element)
        values_list.append(change_type)

    #  checking the length of input values received
    if len(values_list) <= 1:
        print("You need to enter more than 2 digits")
    else:
        print("You have entered", values_list, "elements")
        picking_last_element = values_list[-1]
        print("Last element within list: ", picking_last_element)
        appended_last_element = picking_last_element + 1
        print("Incrementing last element by +1 results: ", appended_last_element)
        values_list.pop()
        values_list.append(appended_last_element)
        print(values_list)


# calling function
increment_array_element()
