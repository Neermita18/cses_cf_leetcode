class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        h={}
        for x in range(len(nums)):
            if nums[x] in h and abs(h[nums[x]]-x)<=k:
                return True

            h[nums[x]]=x
        return False