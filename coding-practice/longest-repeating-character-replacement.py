class Solution(object):
    def characterReplacement(self, s, k):
        max_length = 0
        max_freq = 0

        frequencies = {}

        l = 0
        r = 0

        while r < len(s):
            frequencies[s[r]] = 1 + frequencies.get(s[r], 0)
            max_freq = max(max_freq, frequencies[s[r]])

            while (r - l + 1) - max_freq > k:
                frequencies[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)
            r += 1

        return max_length