class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        profit = 0
        while i < len(prices)-1:
            if prices[i+1] >= prices[i]:
                profit += prices[i+1] - prices[i]
            i += 1
        return profit