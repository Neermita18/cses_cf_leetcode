class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        heights=[]
        heights.append(0)
        for x in range(0, len(gain)):
            y = heights[len(heights)-1]
            s= y + gain[x]
            heights.append(s)
        heights.sort()
        print(heights)
        return heights[len(heights)-1]