       

def bo(a, input):
    pre=""
    post=""
    for i in range(0, a-1):
        
        pre=input[0:i+1]
        post=input[i+1:a]
        l1=0
        l2=0
        on1=0
        on2=0
        cx=0
        for j in range(0, i+1):
            if(pre[j]=='O'):
                on1=on1+1
            else:
                l1=l1+1
        for j in range(0, a-i-1):
            if(post[j]=='O'):
                on2=on2+1
            else:
                l2=l2+1    
        if(on1!=on2 and l1!=l2):
            print(i+1)
            break
        else:
            cx=cx+1   
        # print(pre)
        # print(post)
        # print("*********")
    if cx!=0:
        print("-1")  


size_input = int(input())

# Taking input for the string itself
string_input = input()

# Calling the function with the input values
bo(size_input, string_input)
# st="LLOOOOLLLO"   
# bo(st)    