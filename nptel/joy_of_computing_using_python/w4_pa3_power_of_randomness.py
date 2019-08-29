'''
29/08/2019
You all have used the random library of python. You have seen in the screen-cast of how powerful it is.
In this assignment, you will sort a list let's say list_1 of numbers in increasing order using the random library.

Step 1: Import the randint definition of the random library of python. Check this page if you want some help.
Step 2: Take the elements of the list_1 as input.
Step 3: randomly choose two indexes i and j within the range of the size of list_1.
Step 4: Swap the elements present at the indexes i and j. After doing this, check whether the list_1 is sorted or not.
Step 5: Repeat step 3 and 4 until the array is not sorted.

Input Format:
The first line contains a single number n which signifies the number of elements in the list_1.
From the second line, the elements of the list_1 are given with each number in a new line.

Output Format:
Print the elements of the list_1 in a single line with each element separated by a space. 
NOTE 1: There should not be any space after the last element.

Example:    Input:      4
                        3
                        1
                        2
                        5

            Output:     1 2 3 5

Explanation: 
The first line of the input is 4. Which means that n is 4, or the number of elements in list_1 is 4. The elements of list_1 are 3, 1, 2, 5 in this order.
The sorted version of this list is 1 2 3 5, which is the output.
'''
from random import randint # import random library
n = int(input())
my_list = []
# uppend inputs into list
for i in range(n):
    x = int(input())
    my_list.append(x)


flag = 1

while(flag):
    # randomly chooses two values into variables using radint function
    i = randint(0, n-1)
    j = randint(0, n-1)
    # swapping two indexes each other
    my_list[i], my_list[j] = my_list[j], my_list[i]

    # checking if list is sorted or not
    for k in range(n-1):
        if(my_list[k] > my_list[k+1]):
            # flag becomes 0 if not sorted
            flag = 0
            
    # if flag is 1(sorted) exit while loop, otherwise set flag = 1 and repeat swapping
    if(flag == 1):
        break
    else:
        flag = 1

# printing list
for i in range(n):
    if(i < n-1):
        print(my_list[i], end = " " )
    else:
        print(my_list[i], end = "" )
