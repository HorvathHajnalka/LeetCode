class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        maxh = 0
        curr = 0
        for alt in gain:
            curr += alt
            if curr > maxh:
                maxh = curr
        return maxh
        