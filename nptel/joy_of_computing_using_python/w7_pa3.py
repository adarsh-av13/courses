'''
Binary Matrix 
Given a matrix with N rows and M columns, the task is to check if the matrix is a Binary Matrix. 
A binary matrix is a matrix in which all the elements are either 0 or 1.

Input Format:   The first line of the input contains two integer number N and M which represents the number of rows and the number of columns respectively, separated by a space.
                From the second line, take N lines input with each line containing M integer elements with each element separated by a space. 

Output Format:  Print 'YES' or 'NO' accordingly

Example:    Input:  3 3
                    1 0 0
                    0 0 1
                    1 1 0
            Output: YES 

Solution:   
def isBinaryMatrix(mat,M,N): 
    for i in range(M): 
        for j in range(N): 
            # Returns false if element 
            # is other than 0 or 1. 
            if ((mat[i][j] == 0 or mat[i][j] == 1)==False): 
                return False; 
  
    # Returns true if all the  
    # elements are either 0 or 1. 
    return True; 

a,b=map(int,input().split())


m = []
for i in range(1,a+1):    
    l = list(map(int, input ().split ()))
    m.append(l)
if (isBinaryMatrix(m,a,b)): 
    print("YES")
else: 
    print("NO")
'''



x,y = map(int,input().split())
a=[list(map(int,input().split())) for i in range(x)];
msg='YES';
for i in range(x):
  for j in range(y):
    if(a[i][j]!=0 and a[i][j]!=1):
      msg='NO';
      break;
  if(msg=='NO'):
    break;
print(msg,end='')