class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        c=0
        for x in nums:
            if x==val:
                c+=1
        for x in range(c):
            nums.remove(val)      
    
        ## nums = [x for x in nums if x != val]