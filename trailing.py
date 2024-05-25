def get_trailing_zeroes(n):
    zeroes = 0 
    while n > 0:
        n //= 5
        zeroes += n
    print(zeroes)
    
    
n= int(input())
get_trailing_zeroes(n)