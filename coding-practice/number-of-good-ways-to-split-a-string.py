class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        repetitions = {}
        for i in range(0, len(s)):
            if s[i] not in repetitions:
                repetitions[s[i]] = 1
            else:
                repetitions[s[i]] += 1
        splits = 0
        left = 0
        right = len(repetitions)
        appeared = set()
        for i in range(0, len(s)):
            appeared.add(s[i])
            repetitions[s[i]] -= 1
            if repetitions[s[i]] == 0:
                right -= 1
            if len(appeared) == right:
                splits += 1
        return splits