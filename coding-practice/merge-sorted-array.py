class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i1 = m - 1
        i2 = n - 1
        curr = (m + n) - 1

        while i2 >= 0:
            if i1 >= 0 and nums1[i1] >= nums2[i2]:
                nums1[curr] = nums1[i1]
                curr -= 1
                i1 -= 1
            else:
                nums1[curr] = nums2[i2]
                curr -= 1
                i2 -= 1