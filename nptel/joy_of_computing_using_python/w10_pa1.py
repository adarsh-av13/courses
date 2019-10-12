'''
Special Character  
Given a string S, check whether it contains any special character or not. Print 'YES' if it does else 'NO'.

Input Format:   The first line contains the string S
Output Format:  Print 'YES' or 'NO'

Example:    Input:  Hi$my*name
            Output: YES 

Solution:   

import re 
  
# Function checks if the string 
# contains any special character 
def run(string): 
  
    # Make own character set and pass  
    # this as argument in compile method 
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
      
    # Pass the string in search  
    # method of regex object.     
    if(regex.search(string) == None): 
        print("NO") 
          
    else: 
        print("YES")

S = input()

run(S)
'''


special_charachter = ['~', '`', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', '\'', '<', '>', ',', '.', '?', '/']
flag = 0
x = input()
for i in x:
  if i in special_charachter:
    flag = 1
if (flag == 1):
    print('YES', end='')
else:
    print('NO', end='')