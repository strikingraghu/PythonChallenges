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

def calculate_timings():
    print()

    # user input validation and assessment
    total_sum = 0
    incoming_values = input("Enter any 2 positive numbers: ").split()
    for each_num in incoming_values:
        int_type_conversion = int(each_num)
        total_sum = total_sum + int_type_conversion
    print("Sum of both integers provided via User input : ", total_sum)

    # logic to address the problem
    calculate_time = total_sum % 12
    if calculate_time == 0:
        print("Current time is exactly 00.00 Hours")
    else:
        print("Current time is", calculate_time, "O'clock")


# calling function
calculate_timings()
