class Solution(object):
    def removeDuplicates(self, nums):
        r = 1
        l = 0
        repeated = False
        while r < len(nums):
            if nums[r] != nums[r-1]:
                l += 1
                nums[l] = nums[r]
                repeated = False
            elif nums[r] == nums[r-1] and not repeated:
                l += 1
                nums[l] = nums[r]
                repeated = True
            r += 1
        return l + 1
