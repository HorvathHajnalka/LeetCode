class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hash_map = {}
        for num in arr:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        s = set()
        for k in hash_map:
            s.add(hash_map[k])
        if len(s) == len(hash_map):
            return True
        else:
            return False