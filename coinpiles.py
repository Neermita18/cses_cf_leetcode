def coinpiles(a,b):
    
    
    # while(a>=0 and b>=0):
        if a>b:
            if 2*b<a:
                print("NO")
            elif (a+b)%3==0  : 
                print("YES")
            else:
                print("NO")
        else:
            if 2*a<b:
                print("NO")
            elif (a+b)%3==0:
                print("YES")
            else:
                print("NO")
    
    


n= int(input())
for i in range(n):
    
    a,b= input().split(" ")
    e=int(a)
    f=int(b)
    coinpiles(e,f)

    
    
