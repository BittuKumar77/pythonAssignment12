# 10. Write a python script to calculate HCF of two numbers

num1=int(input("Enter 1st Number:"))
num2=int(input("Enter 2nd Number:"))

if num2>num1:
    mn=num1
else:
    mn=num2
for i in range(1,mn+1):
    if (num1%i==0) and (num2%i==0):
        hcf=i
print("HCF of two numbers:",hcf)