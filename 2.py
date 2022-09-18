# 2. Write a python script to check whether a given number is Prime or not

n=int(input("Enter a number:"))
for i in range(2,n):
    if n%i==0:
        print("this number is not prime")
        break
    else:
        print("This number is prime")
        break