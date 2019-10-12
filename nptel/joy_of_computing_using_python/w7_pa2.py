'''
Symmetric
Given a square matrix of N rows and columns, find out whether it is symmetric or not.

Input Format:   The first line of the input contains an integer number n which represents the number of rows and the number of columns.
                From the second line, take n lines input with each line containing n integer elements with each element separated by a space.

Output Format:  Print 'YES' if it is symmetric otherwise 'NO'

Example:    Input:  2
                    1 2
                    2 1
            Output: YES 

Solution:   

def isSymmetric(mat, N): 
    for i in range(N): 
        for j in range(N): 
            if (mat[i][j] != mat[j][i]): 
                return False
    return True
   

a = int(input())


m = []
for i in range(1,a+1):    
    l = list(map(int, input ().split ()))
    m.append(l)
if (isSymmetric(m, a)): 
    print("YES")
else: 
    print("NO")
'''


n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
i=0
msg='YES'
while(i<n-1):
  j=i+1
  while(j<n):
    if(a[i][j]!=a[j][i]):
      msg='NO'
      break
    j=j+1
  i=i+1
print(msg,end='')