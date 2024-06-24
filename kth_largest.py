import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap=[]
        for x in nums:
            heapq.heappush(heap, -x)
        for i in range(k-1):
            heapq.heappop(heap)
        x=heapq.heappop(heap)
        print(-x)
        return -x