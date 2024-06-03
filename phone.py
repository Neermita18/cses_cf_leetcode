import math
o= int(input())
for w in range(o):
    x= input().split(" ")
    a= int(x[0])
    b= int(x[1])
    initial_screens=math.ceil(b/2)
    def func(a,b):
    
        l=[]
        for i in range(initial_screens):
            l.append(2)
        sum=0
        for i in l:
            sum= sum+i
            # print(sum)
        if sum == b+1:
            l[len(l)-1]=1
        # print(l)
        sum2=0
        for i in l:
            sum2= sum2+i
        sum2*=4
        # print(sum2)
        total=15*initial_screens
        # print(total)
        left= total-sum2
        if a<=left:
            print(initial_screens)
        else:
            # print(a-left)
            print(initial_screens+math.ceil((a-left)/15))          
    func(a,b)      
        

        
        