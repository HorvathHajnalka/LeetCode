class Solution(object):
    def lengthOfLongestSubstring(self, s):
        subset = set()
        maxlen = 0
        l = 0
        r = 0
        while r < len(s):
            if s[r] in subset:
                maxlen = max(len(subset), maxlen)
                while s[l] != s[r]:
                    l += 1
                l += 1
                subset = set(s[l:r + 1])
            else:
                subset.add(s[r])
                print(subset)
                if r == len(s) - 1:
                    maxlen = max(len(subset), maxlen)
            r += 1

        return maxlen
        