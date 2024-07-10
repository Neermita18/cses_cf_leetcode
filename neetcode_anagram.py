class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h={}
        h2={}
        if len(s)!=len(t):
            return False
        for x in s:
            h[x]=h.get(x,0)+1
        print(h)
        for x in t:
            h2[x]=h2.get(x,0)+1
        for x in t:
            if x not in s or h2[x]!=h[x]:
                return False
                break
        return True