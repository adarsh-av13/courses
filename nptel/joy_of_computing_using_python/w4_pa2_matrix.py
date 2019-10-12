'''
29/08/2019
Matrix 
You are provided with the number of rows (R) and columns (C).
Your task is to generate the matrix having R rows and C columns such that all the numbers are in increasing order starting from 1 in row wise manner.

Input Format:	The first line contain two numbers R and C separated by a space.
Output Format:	Print the elements of the matrix with each row in a new line and elements of each row are separated by a space.

NOTE: There should not be any space after the last element of each row and no new line after the last row.

Example:    Input:      3 3

            Output:     1 2 3
                        4 5 6
                        7 8 9

Explanation:	Starting from the first row, the numbers are present in the increasing order. Since it's a 3X3 matrix, the numbers are from 1 to 9.

Solution:

a,b=map(int,input().split())

count=1
m = []
for i in range(1,a+1):
    l = []
    for j in range(1,b+1):
        l.append(count)
        count+=1
    m.append(l)

for i in range(a):
    for j in range(b):
        if(j==b-1):
            print(m[i][j], end="")
        else:
            print(m[i][j], end=" ")
    if(i!=a-1):
        print()
'''

# reading no. of row and column from user in the same line into r and c
r, c = [int(x) for x in input().split()]
my_matrix = []		# initializing a matrix
limit = r *             # no of elements in the list
count = 1

# insert into matrix upto limit
while (count <= limit):
    for i in range(r):
        # create a new list and add elements one by one
        l = []
        for j in range(c):
            l.append(count)
            count = count + 1
        # add the row 'l' to a new list 'my_matrix'
        my_matrix.append(l)

# printing elements
for i in range(r):
    for j in range(c):
            # print element of row upto second last element
            if (j < c-1):
                print(my_matrix[i][j], end = " ")
            else:
                # if element is last one, print it alone
                if(my_matrix[i][j] == my_matrix[-1][-1] ):
                    print(my_matrix[i][j], end = "")
                # else print element and new line
                else:
                    print(my_matrix[i][j], end = "")
                    print()







