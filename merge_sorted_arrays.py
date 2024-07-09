class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.

        """
        heap=[]
        import heapq
        for i in range(m):
                heapq.heappush(heap,nums1[i])
        for j in range(n):
                heapq.heappush(heap,nums2[j])
        print(heap)
        for k in range(m + n):
            nums1[k] = heapq.heappop(heap)