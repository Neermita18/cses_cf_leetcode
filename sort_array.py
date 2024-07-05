class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import heapq
        heap=[]
        a=[]
        for x in nums:
            heapq.heappush(heap,x)
        for i in range(len(heap)):
            a.append(heapq.heappop(heap))
        return(a)