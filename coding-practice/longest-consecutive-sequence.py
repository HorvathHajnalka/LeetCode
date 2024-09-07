class Solution(object):
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        max_length = 0

        for num in nums:
            if num-1 not in nums_set:
                curr_length = 1
                curr = num
                while curr + 1 in nums_set:
                    curr_length += 1
                    curr += 1
                max_length = max(max_length, curr_length)
        
        return max_length