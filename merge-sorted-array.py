class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        if m == 0:
            for idx in range(0, len(nums2)):
                nums1[idx] = nums2[idx]

        i =  m - 1 # 0
        j = n - 1 # 0
        k = n + m - 1 # 1
        while k >= 0:
            if  j >= 0 and (i < 0 or nums2[j] > nums1[i]):
                    nums1[k] = nums2[j]
                    j -= 1

            elif i >= 0:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
            
            