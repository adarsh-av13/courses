'''
24-08-2019
Given a list of numbers (integers), find second maximum and second minimum in this list.

Input Format:   The first line contains numbers separated by a space.

Output Format:  Print second maximum and second minimum separated by a space

Example:    Input:  1 2 3 4 5
            Output: 4 2

Solution:
    a = [int(x) for x in input().split()]
    a.sort() #this command sorts the list in ascending order
    print(a[-2],a[1])
'''

# read multiple inputs as a single line into an array x
x = list(map(int, input().split()))

# sort the array
x.sort()

# print second last(index is -2) and second(index  is 1) element in the array
print(x[-2], x[1], end="")
