'''
26/08/2019
Given an integer number n, you have to print the factorial of this number. To know about factorial please click on this link.

Input Format:	A number n.
Output Format:	Print the factorial of n.
'''
n = int(input())
fact = 1
while 1 < n:
    fact = fact * n
    n = n - 1
print(fact, end="")
