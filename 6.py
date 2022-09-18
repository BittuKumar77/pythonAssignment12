# 6. Write a python script to print first N prime numbers

n =  int(input("Enter the number:"))
a=2
while n!=0:
    for i in range(2,a):
        if a%i==0:
            break
    else:
        print(a,end=' ')
        n-=1
    a+=1    
