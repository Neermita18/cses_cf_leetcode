class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        hash1=[0]*26
        hash2=[0]*26
        i=j=0
        for x in word1:
            hash1[ord(x)-ord('a')]+=1
        for x in word2:
            hash2[ord(x)-ord('a')]+=1
        print(hash1)
        print(hash2)
        if set(hash1)!=set(hash2):
            return False
        for i in range(26):
            if (hash1[i] == 0 and hash2[i] != 0) or (hash1[i] != 0 and hash2[i] == 0):
                return False

        hash1.sort()
        hash2.sort()
        # print(hash1)
        # print(hash2)
        

        for x in range(len(hash1)):
            if hash1[x]!=hash2[x]:
                return False
        return True

