class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h={}
        # n=sum(nums)
        for i in range(len(nums)):
            h[nums[i]]=i
        for i in range(len(nums)):
            n=target-nums[i]
            if n in h and h[n]!=i:
                return [i, h[n]]