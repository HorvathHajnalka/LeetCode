class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = nums
        multiplication_all = 1
        zeros = 0
        for j in range(0, len(nums)):
            if nums[j] != 0:
                multiplication_all *= nums[j]
            else:
                zeros += 1
        for i in range(0, len(answer)):
            if answer[i] != 0 and zeros == 0:
                answer[i] = multiplication_all/answer[i]
            elif answer[i] == 0 and zeros == 1:
                answer[i] = multiplication_all
            else:
                answer[i] = 0
            
        return answer