def power(s):
    for d in s:
        x=int(d)
        c=2
        for i in range(2, x):
            if x%i==0:
                c+=1
        print(c)       
        
n = int(input())

for i in range(n):
    s=input().split("\n")
    
    power(s)