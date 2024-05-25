def distinct(n, s):
    x=sorted(s) #had tried using set() first, but that also exceeded time. Sorting reduces time complexity
    c=1
    star=x[0]
    
    for i in x[1:]:
        if i != star:
            c+=1
            star=i
    print(c)
    
    
n = int(input())
s = []

s= list(map(int, input().split(" ")))


distinct(n, s)