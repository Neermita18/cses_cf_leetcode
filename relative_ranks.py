import heapq
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        d={}
        heap=[]
        for x in score:
            heapq.heappush(heap,-x)
        # print(heap)
        places=["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i in range(3,len(score)):
            places.append(str(i+1))
            i-=1
        print(places)
        for x in range(len(score)):
            y=-heapq.heappop(heap)
            d[y]=places[x]
        print(d)
        a=[]
        for x in score:
            a.append(d[x])
        # print(a)
        return a