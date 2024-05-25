q= int(input())    
for i in range (0,q):
    
    s= input().split(" ")
 

    a= int(s[0])
    b= int(s[1])
    c= int(s[2])
    d= int(s[3])
    # print(a,b,c,d)
    if (c==a or c==b or d==a or d==b):
        print("NO")
    else:
        array= [1,2,3,4,5,6,7,8,9,10,11,12]
        a1= max(a,b)
        b1= min(a,b)
        larger= [x for x in array if (int(x)>a1 or int(x)< b1)]
        smaller= [x for x in array if int(x)<= a1 and int(x)>=b1]
        # print(smaller, larger)

        if ((c not in larger and d not in larger)  or (c not in smaller and d not in smaller) ):
            print("NO")
        else:
            print("YES")
