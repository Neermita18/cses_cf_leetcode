class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=max(nums)
        curMin, curMax=1,1
        for x in nums:
            if x==0:
                curMin, curMax=1,1
                continue
            t=curMax*x
            curMax= max(x*curMax, x*curMin, x)
            curMin= min(t, x*curMin, x)

            res=max(res, curMax)
        return res
        