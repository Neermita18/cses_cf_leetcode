def  check(n):
        
    if n%2==0:
        return True
    else:
        return False
def weird(n):
    if n==1:
        print(int(n))
    else:
        print(int(n))
        
        if check(n):
            n= n/2
            weird(n)
        else:
            n= n*3+1
            weird(n)
               
n=0  
n = int(input())

weird(n)