class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c=0
        for x in nums:
            if x==0:
                c+=1
        for x in range(c):
            nums.remove(0)
        for x in range(c):
            nums.append(0)
        