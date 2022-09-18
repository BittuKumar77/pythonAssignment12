# 3. Write a python script to print all Prime numbers under 100

p=[]
for i in range(2,101):
    if all(i%p for p in p):
        print(i,end = ' ')
        p.append(i)