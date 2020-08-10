"""
Problem Link: https://practice.geeksforgeeks.org/problems/12-hour-clock-addition/0
Given two positive integers num1 and num2, the task is to find the sum of the two numbers on a 
12 hour clock rather than a number line.
Input
First line of the input contains an integer T denoting the number of test cases. 
For each test case there will be single line containing two space seperated integers.
Output
Corresponding to each test case, print the sum in a new line.
Constraints:
1 <= T <= 100
0 <= num1 <= 50
0 <= num2 <= 50
Example:
Input:
2
7 5
3 5
Output
0
8
"""


def num_sum_12_hour_clock():
    print()

    values_list = []
    incoming_values = [int(x) for x in input("Enter 2 numbers: ").split()]
    for each_num in incoming_values:
        values_list.append(each_num)
        if each_num >= 0:
            pass
        else:
            print("Please enter positive numbers only!")
            break
    

    if len(values_list) <= 1:
        print("Please enter only 2 digits")
    elif len(values_list) >= 3:
        print("Dont enter more than 2 values")
    else:
        print("Thanks for entering 2 digits")
    
    
    total_result = values_list[0] + values_list[1]
    if total_result < 12:
        print("Sum of both numbers are within the value 12 and result is: ",total_result)
    else:
        print("Sum of both numbers are beyond the value 12 and result is: ", total_result % 12)


# calling function
num_sum_12_hour_clock()
