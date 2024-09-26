class Solution(object):
    def findMin(self, nums):
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2 
        while l < r:
            m = (l + r) // 2 
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]