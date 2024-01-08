class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','A', 'e','E', 'i','I', 'o','O', 'u', 'U']
        returnword = []
        invowels = []
        for i in range(0, len(s)):
            if s[i] in vowels:
                invowels.append(s[i])
                returnword.append( 0)
            else:
                returnword.append(s[i])
        for i in range(0, len(returnword)):
            if returnword[i] == 0:
                returnword[i] = invowels[-1]
                del invowels[-1]
        returnstr = ""
        returnstr = returnstr.join(returnword)
        return returnstr