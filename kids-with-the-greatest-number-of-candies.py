class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        maxcandy = max(candies)
        for number in candies:
            if number + extraCandies >= maxcandy:
                result.append(True)
            else:
                result.append(False)
        return result