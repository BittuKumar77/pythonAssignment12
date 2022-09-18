# 8. Write a python script to print first N terms of a Fibonacci series

n=int(input("Enter a number:"))
x=0
y=1
z=0
while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y