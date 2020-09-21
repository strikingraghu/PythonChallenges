"""
Given a list of characters, merge all of them into a string.
Input:
First line of the input contains an integer T, denoting the number of testcases.
Then T test case follows. Each testcase contains two lines:-
The number of characters in the array N.
The array of characters separated by space
Output:
For each testcase, print the character array converted into a string.

Sample Input:
2
13
g e e k s f o r g e e k s
11
p r o g r a m m i n g
Sample Output:
geeksforgeeks
programming
"""


def form_english_word():
    print()

    incoming_tests = int(input("Enter the number of test cases you are willing to run: "))
    while incoming_tests > 0:
        incoming_chars = input("Enter any english characters to form a word: ").split()
        word_formation = ""
        for each_element in incoming_chars:
            word_formation = word_formation + each_element
        print("All whitespaces are removed and formed a word: ", word_formation)
        incoming_tests -= 1


# calling functions
form_english_word()


"""
Problem Link: https://practice.geeksforgeeks.org/problems/check-for-binary/1
Given a non-empty sequence of characters, return true if sequence is Binary, else return false

Input:
The task is to complete the method that takes a string as argument. We should not read any input from stdin/console. 
There are multiple test cases. For each test case, this method will be called individually.
Output:
Your function should return true str is binary, else false
Constraints:
1<=T<=50
1<=Length of str<=10000

Example:
Input:
2
101
75
Output:
1
0
"""


def check_binary():
    print()

    testcases = int(input())
    for i in range(testcases):
        incoming_num = input().strip()
        if is_binary(incoming_num):
            print("It's a binary number!")
        else:
            print("It's not a binary number!")


def is_binary(incoming_num):
    for i in incoming_num:
        if i not in "01":
            return False
    return True


# calling function
check_binary()
