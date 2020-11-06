"""
You are given an integer input N and you have to find whether it is Anshuman’s favourite or not.
If it is then print “YES” else print “NO”.
A number is Anshuman’s favourite if it's either the sum or the difference of the integer 5. (5+5, 5+5+5, 5-5, 5-5-5+5+5)

Input:
The first line of input contains an integer denoting the number of test cases.
Next line of input contains an integer N to be tested.

Output:
For each test case , the output is in a new line containing the answer 'YES' or 'NO' depending on whether the
given number N is Anshuman's favourite or not.

Constraints:
1<=T<=100
-10^9<=N<=10^9

Example:
Input :
1
10
Output :
YES
Because 10 can be written as a sum of 5+5.
"""


def divisible_validation():
    print()

    values_list = []
    incoming_values = [int(x) for x in input("Enter any 2 positive digits: ").split()]
    #  each value is been appended to the list
    for each_user_val in incoming_values:
        converting_type = int(each_user_val)
        values_list.append(converting_type)
    if len(values_list) <= 1:
        print("Please enter minimum 2 digits")

    #  validating the input values for positive or negative numbers
    polled_element = 0
    for every_val in values_list:
        if every_val > 0:
            polled_element = polled_element + 1
            continue
    if polled_element == len(values_list) & len(values_list) == 2:
        print("All the numbers provided are positive in nature")
        for each_element in values_list:
            if each_element % 5 == 0:
                print("You did enter", each_element, "and it's divisible by 5")
            else:
                print("You did enter", each_element, "and it's not divisible by 5")
    else:
        print("One of the number provided is negative number and doesn't meet an user input prerequisites")


# calling function
divisible_validation()
