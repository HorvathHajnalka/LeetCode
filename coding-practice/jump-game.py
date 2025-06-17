class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        maxidx = 0
        i = 0
        while i < size - 1 and maxidx < size - 1:
            maxidx = max(maxidx, i + nums[i])
            if maxidx < i + 1:
                return False
            i += 1
        return True