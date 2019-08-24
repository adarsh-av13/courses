'''
24-08-2019
Given a list A of numbers (integers), you have to print those numbers which are not multiples of 5.

Input Format:   The first line contains the numbers of list A separated by a space.

Output Format:  Print the numbers in a single line separated by a space which are not multiples of 5.

Example:    Input:  1 2 3 4 5 6 5
            Output: 1 2 3 4 6

Solution:
    a = [int(x) for x in input().split()]  
    b = []
    for i in a:
        if(i%5!=0):
            b.append(i)
    for i in range(len(b)):
        if(i==len(b)-1):
            print(b[i],end="")
        else:
            print(b[i],end=" ")
'''

# read multiple inputs seperated by space into an array x
user_inputs = list(map(int, input().split()))

# initialize array to store numbers which are not multiples of 5
not_multiples = []

# if element is not multiple of 5, then append it to 'not_multiples' array
for i in user_inputs:
    if(i % 5 != 0):
        not_multiples.append(i)
        
# print elements of the array 'not_multiples', except last element seperated by a space
for i in range(len(not_multiples) - 1):
    print(not_multiples[i], end = " ")
    
# print last element of the array (index is -1)
print(not_multiples[-1], end = "")
