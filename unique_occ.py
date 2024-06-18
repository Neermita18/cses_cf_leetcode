class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c=0
        mydict={}
        for x in arr:
            mydict[x]=0
        print(mydict)
        for x in arr:
            if x in mydict.keys():
                mydict[x]+=1


        print(mydict)
        flag= len(set(mydict.values()))==len(mydict.values())
        if flag:
            return True
        else:
            return False