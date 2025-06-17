class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s

        arr = ['' for x in range(numRows)]
        arr_idx = 0
        s_idx = 0
        backward = False
        while s_idx < len(s):
            arr[arr_idx] += s[s_idx]
            s_idx += 1
            if arr_idx == numRows-1:
                backward = True
            elif arr_idx == 0:
                backward = False
            if backward:
                arr_idx -= 1
            else:
                arr_idx += 1
        return ''.join(arr)