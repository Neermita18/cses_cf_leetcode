class Solution(object):
    def pivotIndex(self, nums):
        # """
        # :type nums: List[int]
        # :rtype: int
        # """
        # right=[]
        # left=[]
        # sum1=0
        # sum2=0
        # for i in range(0, len(nums)-1):
        #     sum1=0
        #     for j in range(i+1, len(nums)):
        #         sum1= sum1+nums[j]
        #     right.append(sum1)
        # right.append(0)
      

        # nums2= nums[::-1]

        # for i in range(0, len(nums)-1):
        #     sum2=0
        #     for j in range(i+1, len(nums)):
        #         sum2= sum2+nums2[j]
        #     left.append(sum2)
        # left.append(0)
        # left= left[::-1]
    
        # for x in range(len(nums)):
        #     if left[x]==right[x]:
        #         return x
        # return -1
        sum1= sum(nums)
        print(sum1)
        left= 0
        for i in range(len(nums)):
            right= sum1-left-nums[i]
            if left==right:
                return i
            left+=nums[i]
        return -1