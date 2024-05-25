def rep(s):
    # x=""
    # x= ''.join(sorted(s))
    # x= sorted(s)
    #print(x) 
    n= len(s)
    a=[]
   
    c=0
    j=0
    i=1
    st=0
    if n==1:
        
        a.insert(st,c)  
    else:
        while i<n and j<n-1 and n>1:
            if s[i]==s[j] and i!=n-1 and j!=n-2:
        
                c+=1
            #print(c)
            
                j+=1
                i+=1
            elif s[i]==s[j] and i==n-1 and j==n-2:
            
                c+=1
                a.insert(st, c)
            
            
            
                break
        
            else:
                a.insert(st, c)
            
                st+=1
                c=0
           
                i+=1
                j+=1
          
 
    maxi(a)
def maxi(a) :
    max= a[0]
    for i in a:
        if i>max:
            max=i
    print(max+1)  
                       
s= input()
rep(s)



