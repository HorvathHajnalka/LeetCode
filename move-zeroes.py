class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        i = 0
        j = 0
        while i < len(nums)-2:
            j = i + 1
            if nums[i] == 0:
                while nums[j] == 0:
                    j += 1
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
            i += 1
            """
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                del nums[i]
                count += 1
            else:
                i += 1
        for i in range(0, count):
            nums.append(0)