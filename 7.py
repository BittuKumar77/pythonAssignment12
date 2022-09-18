# 7. Write a python script to check whether a given pair of numbers are co-Prime
# numbers or not.

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))

x=min(a,b)
for i in range(1,x+1):
    if a%i==0 and b%i==0:
        hcf=i
        
if hcf==1:
    print("This is Co-prime number")
else:
    print("This is not Co-prime number")
