class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        s1=set()
        s2=set()
       
        for x in nums1:
            if x not in nums2:
                s1.add(x)
        for x in nums2:
            if x not in nums1:
                s2.add(x)
        print(s1,s2)
        s1=list(s1)
        s2=list(s2)
        return [s1,s2]