# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        high=n
        low=1
        while low<=high:
            mid= (low+high)//2
            s=guess(mid)
            if s==0:
                return mid
            if s==-1:
                high=mid-1
            if s==1:
                low=mid+1