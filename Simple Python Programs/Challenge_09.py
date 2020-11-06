"""
Problem Link: https://practice.geeksforgeeks.org/problems/anagram/0
Given two strings, check whether two given strings are anagram of each other or not. An anagram of a string is another 
string that contains same characters, only the order of characters can be different. For example, “act” and “tac” are 
anagram of each other.

Input: 
The first line of input contains an integer T denoting the number of test cases. Each test case consist of two strings 
in 'lowercase' only, in a single line.

Output:
Print "YES" without quotes if the two strings are anagram else print "NO".

Constraints:
1 ≤ T ≤ 30
1 ≤ |s| ≤ 1016

Example:
Input:
2
geeksforgeeks forgeeksgeeks
allergy allergic

Output:
YES
NO
"""
import collections


def anagram_string_validations():
    print()
    incoming_strings = input("Enter any 2 strings with a space between them: ").split()

    # taking both values to an array
    first_arr = incoming_strings[0]
    second_arr = incoming_strings[1]

    # sorting elements
    sorted_first_arr = sorted(first_arr)
    sorted_second_arr = sorted(second_arr)

    # comparison check
    if sorted_first_arr == sorted_second_arr:
        print("Entered 2 values are anagram!")
    else:
        print("Entered 2 values are not anagram@")


def validate_anagram_pattern():
    print()
    incoming_values = input("Enter any 2 specific strings: ").split()

    # taking incoming values to a list
    first_list = incoming_values[0]
    second_list = incoming_values[1]

    letters = collections.defaultdict(int)
    for i in first_list:
        letters[i] += 1
    for i in second_list:
        letters[i] -= 1
    
    if letters[i] < 0:
        print("Entered values are not anagram!")
    else:
        print("Entered 2 values are anagram!")


# calling functions
anagram_string_validations()
validate_anagram_pattern()
