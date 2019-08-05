"""
Input Format:	The first line of the input contains two numbers separated by a space.
Output Format:	Print the addition in single line

Example:
Input:	4 2
Output:	6

Explanation:	Since the addition of numbers 4 and 2 is 6, hence the output is 6
"""
x, y = input().split()
x = int(x)
y = int(y)
print(x + y, end="")
