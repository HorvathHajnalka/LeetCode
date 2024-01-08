class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merge = ""
        firstbigger = False
        if len(word1) > len(word2):
            size = len(word2)
            firstbigger = True
        else:
            size = len(word1)
        for i in range(0,size):
            merge += word1[i]
            merge += word2[i]
        if firstbigger:
            merge += word1[i+1:]
        else:
            merge += word2[i+1:]
        return merge