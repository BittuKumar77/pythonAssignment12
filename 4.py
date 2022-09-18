# 4. Write a python script to print all Prime numbers between two given numbers (both
# values inclusive)

start =  int(input("Enter 1st number:"))
end =  int(input("Enter lastnumber:"))

for i in range(start,end+1):
    if(i>1):
        for j in range(2,i):
            if((i%j)==0):
                break
            else:
                print(i,end=' ')
                break