class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length = 0
        curr_letters = set()
        l = 0
        r = 0
        while r < len(s):
            if s[r] in curr_letters :
                max_length = max(max_length, len(curr_letters))
                while s[l] != s[r]:
                    l += 1
                l += 1
                curr_letters = set(s[l: r+1]) 
            else:
                curr_letters.add(s[r])
            r += 1
        max_length = max(max_length, len(curr_letters))
        return max_length