class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for x in nums:
            d[x]= d.get(x,0) +1
        print(d)
        import heapq
        heap=[]
        print(len(nums))
        for key, freq in d.items():
            heapq.heappush(heap,(freq, key))
        
            
        print(len(heap))
        while len(heap)!=k:
            heapq.heappop(heap)
        n=[]
        for x in heap:
            n.append(x[1])
        print(n)
        return n