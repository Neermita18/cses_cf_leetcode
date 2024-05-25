def missing(n,a):
    x= sorted(a)
    for i in range(0,n-2):
        if x[i]==i+1:
            continue
        else:
            print(i+1)
            break


n= int(input())
a=[]
for i in range(0, n-2):
    ns= int(input())
    a.append(ns)
    
    
missing(n,a)    
    
    
    
    