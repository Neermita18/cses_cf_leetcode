class Solution(object):
    def getSum(self, x, y):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xffffffff
        while y!=0:
            carry= ((x&y)<<1) & mask
            # print(carry)
            x=(x^y)&mask
            y=carry
        if (x>>31) & 1:
            return x | ~mask
        return x