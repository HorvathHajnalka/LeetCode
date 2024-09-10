class Solution(object):
    def threeSum(self, nums):
        # 10 - 
        triplets = []
        nums.sort()
        i = 0
        while i < len(nums):
            if i > 0 and nums[i-1] == nums[i]:
                i+= 1
                continue
            target = 0
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[left] + nums[right] + nums[i]
                if curr_sum == target:
                    triplet = [nums[i], nums[left], nums[right]]
                    triplets.append(triplet)
                    left += 1
                    while(left < right  and nums[left] == nums[left-1]):
                        left += 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
            i+= 1
        return triplets