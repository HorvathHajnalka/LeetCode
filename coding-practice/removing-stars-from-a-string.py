class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        i = len(s)-1
        afterstar = 0
        while i > -1:
            if s[i] == '*':
                s = s[0:i] + s[i+1:len(s)]
                afterstar += 1
                i-=1
            elif s[i] != '*' and afterstar > 0:
                s = s[0:i-afterstar+1] + s[i+1:len(s)]
                i -= afterstar
            else:
                i -= 1
        return s
        i = len(s)-1
        afterstar = 0
        while i > -1:
            if s[i] == '*':
                s = s[0:i] + s[i+1:len(s)]
                afterstar += 1
            elif s[i] != '*' and afterstar > 0:
                s = s[0:i] + s[i+1:len(s)]
                afterstar -= 1
            i -= 1
        return s
        """
        ret = ""
        i = len(s)-1
        afterstar = 0
        while i > -1:
            if s[i] == '*':
                afterstar += 1
            elif s[i] != '*' and afterstar > 0:
                afterstar -= 1
            else:
                ret += s[i]
            i -= 1
        return ret[::-1] 