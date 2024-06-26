class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones=0
        while n:
            ones= ones+ (n & 1)
            n=n>>1
        print(ones)
        return ones