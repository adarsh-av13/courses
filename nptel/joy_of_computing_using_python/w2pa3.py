# read no of inputs
n = int(input())

# read inputs into a list 'x'
x = list(map(int, input().split()))

# reverse the list and save as another list 'y'
y = x[::-1]

# add each no of both lists
for i in range(n):
    print(x[i] + y[i], end=" ")
