class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = nums
        if not arr:
            return -1
        elif len(arr) <= 4:
            return 0
        else:
            arr.sort() # O(nlogn)
            return min(arr[-4]-arr[0], arr[-3]-arr[1], arr[-2]-arr[2], arr[-1]-arr[3])