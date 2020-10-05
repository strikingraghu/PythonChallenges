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

def incrementing_array():
    print()

    # getting required values from user
    incoming_value_length = input("Enter the number of integers to be part of an array : ")
    incoming_values_array = input("Enter the required numbers : ").split()
    
    # converting values to an integer format
    requested_array_length = int(incoming_value_length)
    converted_int_array = []
    for each_num in incoming_values_array:
        int(each_num)
        converted_int_array.append(each_num)
    print("User provided values in an integer format : ", converted_int_array)

    # performing user input validations
    if len(converted_int_array) == requested_array_length:
        print("Yes, user input is fine! We can proceed further.")
    else:
        print("No, user input isn't meeting requirement! We can't proceed further.")
    
    # final output with new element and getting it increased by +1 value
    sorted_array_elements = sorted(converted_int_array)
    print("Sorting Values = ", sorted_array_elements)
    getting_last_element = sorted_array_elements[-1]
    increased_last_element_value = int(getting_last_element) + 1
    sorted_array_elements.append(increased_last_element_value)
    print("Final Output = ", sorted_array_elements)


# calling function
incrementing_array()
