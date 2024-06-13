class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1<str2:
            s1= (str1)
            s2= (str2)
        else:
            s1= (str2)
            s2= (str1)
        d=[]
        for i in range(1, len(s1)+1):
            if len(s1)%i==0:
                d.append(i)
        sub=[]
        for i in range(1, len(s2)+1):
            if len(s2)%i==0:
                sub.append(i)
        cd=[]
        for i in sub:
            if i in d:
                cd.append(i)
        print(cd)
        listofsub=[]
        listofmain=[]
        final=[]

        for x in cd:
            print(x)
            check= s1[0:x]
            print(check)
            substrings = [s1[i:i+x] for i in range(0, len(s1), x)]
            print(substrings)
            listofsub.append(substrings)
                
            if ( all(sub == check for sub in substrings)):
                substr = [s2[i:i+x] for i in range(0, len(s2), x)]
                listofsub.append(substr) 
        print(listofsub)
        n=(len(listofsub))
        x= listofsub[n-1]
        if all(sub == check for sub in x):
            return (x[0])
        else:
            return ""