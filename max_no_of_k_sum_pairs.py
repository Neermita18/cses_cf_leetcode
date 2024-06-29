class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d={}
        for x in nums:
            x=float(x)
            (d[x])=float(d.get(x,0)+1)
        pairs=0
        a=[]
        for x in d:
            if (k-x) in d and d[x]!=0 and d[k-x]!=0:
                pairs=0
               
                if x==k/2.0:
                    pairs=pairs+ d[x]//2
                    d[x]-=pairs
                 
                    a.append(pairs)
                else:
                    pairs=pairs+ min(d[x], d[k-x])
                   
                    a.append(pairs)
                    d[x]-=pairs
                    d[k-x]-=pairs
           
        return int(sum(a))