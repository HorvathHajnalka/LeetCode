class Solution(object):
    def productExceptSelf(self, nums):
        output = [ 1 for i in range(len(nums))]
        prod = 1

        for i in range(len(nums) - 1):
            prod *= nums[i]
            output[i + 1] = prod
            print(prod)

        prod = 1
        for j in range(len(nums) -1, 0, -1):
            prod *= nums[j]
            output[j - 1] *= prod

        return output