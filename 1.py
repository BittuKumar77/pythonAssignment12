# 1. Write a python script to reverse a number.

n=int(input("Enter a number:"))
a=0
while n!=0:
    x=n%10
    a=a*10+x
    n//=10
print("Reversed is ",a)