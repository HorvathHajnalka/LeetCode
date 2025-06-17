class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        goalidx = len(nums) - 1
        i = 0
        counter = 0
        while i < goalidx:
            if i + nums[i] >= goalidx:
                counter += 1
                goalidx = i
                i = 0
            else:
                i += 1
        return counter