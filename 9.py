# 9. Write a python script to calculate LCM of two numbers

x=int(input("Enter 1st Number:"))
y=int(input("Enter 2nd Number:"))

num = max(x,y)
while(True):
    if(num%x==0 and num%y==0):
        break
    num=num+1
    
print(f"The LCM of ",x,"and" ,y, "is: ",num)