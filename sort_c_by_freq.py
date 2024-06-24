import heapq
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        for x in s:
            d[x]=d.get(x,0)+1
        print(d)
        heap=[]
        for let, freq in d.items():
            heapq.heappush(heap,(-freq,let))
        print(heap)
        a=[]
        for x in range(len(heap)):
            y=(heapq.heappop(heap))
            a.append(y[1]*(-y[0]))
        print(a)
        return "".join(a)