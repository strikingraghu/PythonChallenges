"""
This is a Python Program to print the largest even and largest odd number in a list.

Problem Description
The program takes in a list and prints the largest even and largest off number in it.

Problem Solution
1. Take in the number of elements to be in the list from the user.
2. Take in the elements from the user using a for loop and append to a list.
3. Using a for loop, get the elements one by one from the list
4. Check if it odd or even & append them to different lists.
5. Sort both the lists individually and get the length of each list.
6. Print the last elements of the sorted lists.
7. Exit.
"""


def fetch_largest_even_odd_number():
    print()

    try:
        element_length = int(input("Enter the number of elements you want to push within a list: "))
        setting_range = range(1, element_length+1)
        
        # running loop
        temp_list = []
        for each_loop_val in setting_range:
            fetch_element = int(input("Provide number of your choice: "))
            temp_list.append(fetch_element)
        print("You have entered below values for this code: \n")
        print(temp_list)

        # logic
        even_int_list = []
        odd_int_list = []
        for each_element in temp_list:
            if each_element % 2 == 0:
                even_int_list.append(each_element)
            else:
                odd_int_list.append(each_element)
        even_int_list.sort()
        odd_int_list.sort()
        print("Largest even number provided =", even_int_list[-1], "& Largest odd number provided =", odd_int_list[-1])
    except ValueError as ve:
        print(ve.__context__)


fetch_largest_even_odd_number()
