'''
24-08-2019
You are given a number A which contains only digits 0's and 1's. Your task is to make all digits same by just flipping one digit (i.e. 0 to 1 or 1 to 0 ) only. If it is possible to make all the  digits same by just flipping one digit then print 'YES' else print 'NO'.

Input Format:   The first line contains a number made up of 0's and 1's.

Output Format:  Print 'YES' or 'NO' accordingly without quotes.

Example:    Input:  101
            Output: YES

Solution:
    A = input()
    ls = []
    li = str(A)
    for j in li:
        ls.append(int(j))
    count_z = 0
    count_o = 0
    for k in ls:
        if(k==1):
            count_o += 1
        if(k==0):
            count_z += 1
    if((count_o == 1) or (count_z == 1)):
        print("YES")
    else:
        if((count_o == 0) or (count_z == 0)):
            print("NO")
        else:
            print("NO")
'''


user_input = input()

# initially set no of zeros and ones is 0 
no_of_ones = 0
no_of_zeros = 0

# iterate through input
for i in user_input:
    # if zero or one is found, increment its count
    if i == '0':
        no_of_zeros += 1
    if i == '1':
        no_of_ones += 1

# if 'no of zeros' OR 'no of ones' in input is greater than or equel to 2, print NO, else print YES
if (no_of_zeros or no_of_ones) >= 2:
    print("NO", end = "")
else:
    print("YES", end = "")
