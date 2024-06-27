class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[]
        n=len(nums)
        for k in range(1,n+1):
            new_sum=max_sum=sum(nums[:k])
            # print(max_sum)
            for i in range(0,n-k):
                # print(nums[i])
                # print(nums[i+k])
                new_sum=new_sum-nums[i]+nums[i+k]
                if new_sum>max_sum:
                    max_sum=new_sum
                
            a.append((max_sum,k))
            
        # print(a)
        x,y= max(a)
        z= a.index((x,y))
        # print(x,y,z)
        return x