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
        for _ in setting_range:
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


"""
This is a Python Program to form an integer that has the number of digits at the ten’s place and the least significant
digit in the one’s place.

Problem Description
The program takes an integer and forms a new integer which has the number of digits at the ten’s place and the
least significant digit in the one’s place.

Problem Solution
1. Take in an integer and store it in a variable.
2. Make a separate copy of the integer.
3. Using a while loop, calculate the number of digits in the integer.
4. Convert the copy of the integer and the count of the number of digits to string.
5. Concatenate the last digit of the integer to the count and convert the new integer back to int.
6. Print the newly formed integer.
7. Exit.
"""


def integer_builder():
    print()

    user_input = input("Enter the number of your choice: ")
    user_input_list = []
    integer_length = len(user_input)
    print("Number of integers provided: ", integer_length)
    counter_val = 0
    last_integer = 0
    for each_integer in user_input:
        counter_val = counter_val + 1
        if integer_length == counter_val:
            last_integer = each_integer
        
    building_number = str(integer_length) + str(last_integer)
    print(building_number)


integer_builder()
