class Solution(object):
    def maxOperations(self, nums, k):
        ops = 0
        i = 0
        j = len(nums)-1
        nums.sort()
        while i != j:
            temp = nums[i] + nums[j]
            if temp == k:
                ops+=1
                del nums[i]
                del nums[j-1]
                if j-i > 1:
                    j -= 2
                else:
                    break
            elif temp > k:
                if nums[i] >= nums[j]:
                    i += 1
                else:
                    j -= 1
            elif temp < k:
                if nums[i] >= nums[j]:
                    j -= 1
                else:
                    i += 1
        return ops