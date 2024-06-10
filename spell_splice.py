# https://www.codechef.com/problems/CMIX
# cook your dish here
import math
n = int(input())
l=[]
for i in range(n):
    s= int(input())
    l=[]
    for i in range(s):
        x= input().split(" ")
        a= int(x[0])
        b= int(x[1])
        l.append([a,b])
    list=[]
    # print(l)
    for i in range (0, len(l)-1):
        for j in range(i+1, len(l)):
            n = l[i]
            m= l[j]
            # print(n,m)
            e= n[0]
            f= n[1]
            g= m[0]
            h= m[1]
            list.append(e*h+ f*g)
    print(max(list))
    
    