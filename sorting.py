a= input()
a= int(a)
for i in range(0,a):
    b= (input().split(' '))
    # print(type(b))
    c= int(b[0])
    d=int(b[1])
    print(min(c,d), max(c,d))