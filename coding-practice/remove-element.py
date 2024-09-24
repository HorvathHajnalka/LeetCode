class Solution(object):
    def removeElement(self, nums, val):
        r = 0
        l = 0
        counter = 0
        while r < len(nums):
            if nums[r] == val:
                counter += 1
            else:
                nums[l] = nums[r]
                l += 1
            r += 1
        return len(nums) - counter