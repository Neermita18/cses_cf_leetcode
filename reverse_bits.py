class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        x=bin(n)
       
        x=x[2:]
        
        x=x[::-1] + ("0"*(32-len(x)))
        print(x)
        return int(x,2)