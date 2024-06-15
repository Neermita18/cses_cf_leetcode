class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l= len(s)
        s= list(s)
        if l==0:
            return True
        for x in t:
            if x==s[0]:
                s.remove(x)
                if s==[]:
                    break
        print(s)
        if s==[]:
            return True
        else:
            return False