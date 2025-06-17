class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = max(citations) + 1
        counter = [0 for x in range(length)]
        for c in citations:
            counter[c] += 1
        
        i = length - 1
        countsum = 0
        while i >= 0:
            countsum += counter[i]
            if countsum >= i:
                return i
            else:
                i -= 1
        return 0