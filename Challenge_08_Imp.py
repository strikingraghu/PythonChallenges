"""
Problem Link: https://practice.geeksforgeeks.org/problems/anagram-palindrome/0
Given a string S, Check if characters of the given string can be rearranged to form a palindrome. 
For example characters of “geeksogeeks” can be rearranged to form a palindrome “geeksoskeeg”, but characters of 
“geeksforgeeks” cannot be rearranged to form a palindrome.

Input:
First line consists of integer T  denoting the number of test cases. T testcases follow. For each testcase there are 
one line of input containing string S.

Output:
For each testcase, in a new line, print "Yes" if is possible to make it a palindrome, else "No".

Constraints:
1 <= T <= 100
1 <= |S| <= 1000

Example:

Input:
2
geeksogeeks
geeksforgeeks

Output:
Yes
No
"""


def palindrome_identification_num():
    print()
    incoming_number = int(input("Enter any number greater than zero: "))
    temp_var = incoming_number
    reversed_number = 0
    while incoming_number > 0:
        digit = incoming_number % 10
        reversed_number = reversed_number * 10 + digit
        incoming_number = incoming_number // 10

    # comparison
    if temp_var == reversed_number:
        print("It's a Palindrome")
    else:
        print("It's not a Palindrome")


def palindrome_identification_string():
    print()
    incoming_str = input("Enter any string value: ")
    temp_var = incoming_str[::-1]
    if incoming_str == temp_var:
        print("It's a Palindrome")
    else:
        print("It's not a Palindrome")


# calling functions
palindrome_identification_num()
palindrome_identification_string()
