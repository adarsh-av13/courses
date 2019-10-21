'''
21/10/2019

Letters
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Input Format:   The first line of the input contains a statement.

Output Format:  Print the number of upper case and lower case respectively separated by a space.

Example:    Input:  Hello world!
            Output: 1 9 

Solution:


'''

upper_case = 0
lower_case = 0
ip = input()

for i in ip:
    # if uppercase character
    if i.isupper():
        upper_case += 1
    # # if lowercase character
    if i.islower():
        lower_case += 1
    
print(upper_case, lower_case, end ="")