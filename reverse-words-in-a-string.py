class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = []
        i = 0
        new_word = ''
        while i != len(s):
            if s[i] != ' ' :
                new_word += s[i]
            else:
                if new_word != '':
                    words.append(new_word)
                    new_word = ''
            i += 1
        if new_word != '':
            words.append(new_word)
        rstr = ''
        for i in range(len(words)-1,-1,-1):
            rstr +=  words[i]
            if i != 0:
                rstr += ' '
        return rstr