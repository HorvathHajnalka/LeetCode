class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        curr = 1
        nxt = 1
        i = n - 2
        while i >= 0:
            nxtcalc = nxt + curr
            curr = nxt
            nxt = nxtcalc
            i -= 1
        return nxt