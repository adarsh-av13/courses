'''Given an array A of N numbers (integers), you have to write a program which prints the sum of the elements of array A with the corresponding elements of the reverse of array A.
If array A has elements [1,2,3], then reverse of the array A will be [3,2,1] and the resultant array should be [4,4,4].

Input Format:	The first line of the input contains a number N representing the number of elements in array A.
		The second line of the input contains N numbers separated by a space. (after the last elements, there is no space)
Output Format:	Print the resultant array elements separated by a space. (no space after the last element)

Example:

Input:	4
	2 5 3 1

Output:	3 8 8 3

'''

# read no of inputs
n = int(input())

# read inputs into a list 'x'
x = list(map(int, input().split()))

# reverse the list and save as another list 'y'
y = x[::-1]

# add each no of both lists
for i in range(n):
    print(x[i] + y[i], end=" ")
