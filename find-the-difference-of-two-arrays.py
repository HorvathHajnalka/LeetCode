class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        """
        hash_map = {}
        output = [[],[]]
        for num in nums1:
            hash_map[num] = {1}
        for num in nums2:
            if num in hash_map:
                hash_map[num].add(2)
            else:
                hash_map[num] = {2}
        for numkey in hash_map:
            if len(hash_map[numkey]) == 1:
                if 1 in hash_map[numkey]:
                    output[0].append(numkey)
                if 2 in hash_map[numkey]:
                    output[1].append(numkey)
        return output
        """
        set1 = set(nums1)
        set2 = set(nums2)
        diff1 = list(set1.difference(set2))
        diff2 = list(set2.difference(set1))
        outp = [diff1, diff2]
        return outp