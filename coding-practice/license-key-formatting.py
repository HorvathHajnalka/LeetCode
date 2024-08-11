class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        i = len(s)-1
        arr = []
        while i > -1:
            j = 0
            while j < k and  i > -1:
                if s[i] != '-':
                    arr.append(s[i])
                    j+= 1
                    i -= 1
                else:
                    i -= 1
            arr.append('-')
        while arr and arr[-1] == '-':
            del arr[-1]

        return ''.join(arr[::-1]).upper()
        