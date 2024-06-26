class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans=[]
        for x in range(0, n+1):
            s=bin(x)[2:]
            ones=0
            print(type(s))
            for i in s:
                ones+=int(i)
            print(ones)
            ans.append(ones)
        return (ans)
        