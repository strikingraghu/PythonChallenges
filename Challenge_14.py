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
