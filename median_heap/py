import heapq
class MedianFinder(object):


    def __init__(self):
        self.nums=[]
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.nums, num)
        

    def findMedian(self):
        """
        :rtype: float
        """
        a=[]
        for x in range(len(self.nums)):
            x=heapq.heappop(self.nums)
            a.append(x)
        
        if len(a)%2==0:
            x=len(a)/2
            y=(len(a)/2)-1
            n=(a[x]+a[y])/2.0
            for x in a:
                heapq.heappush(self.nums,x)
            return n
        else:
            m=a[len(a)/2]
            for x in a:
                heapq.heappush(self.nums,x)
            return m
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()