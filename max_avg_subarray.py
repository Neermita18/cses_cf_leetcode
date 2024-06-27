class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n=len(nums)
        
        maxi=new_sum=sum(nums[:k])
        for i in range(n-k):
            new_sum= new_sum-nums[i]+nums[i+k]
            if new_sum>maxi:
                maxi=new_sum
        return maxi/float(k)