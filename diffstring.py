a= int(input())
for i in range(0, a):
    s= input()
    l= len(s)
    a= s[0]
    c=0
    t=''
    for i in range(1, len(s)):
        if s[i]!=a:
            c+=1
            s1= list(s)
            s1[i]=a
            s1[0]=s[i]
        
            

            break
        else:
            c=0
        
    if c!=0:
        print("YES")
        
      
        print("".join(s1))
        
        
    else:
        print("NO")
        