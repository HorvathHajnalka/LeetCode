class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0 for i in range(n+1)]
        current_power_of_two = 0
        next_power_of_two = 1
        for i in range(n+1):
            if i == next_power_of_two:
                current_power_of_two = next_power_of_two
                next_power_of_two = current_power_of_two * 2
            if i != 0:
                ans[i] = 1 + ans[i - current_power_of_two]
        return ans
