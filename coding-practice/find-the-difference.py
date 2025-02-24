class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        """
        # dictionary approach
        t_letter_count = dict()
        for letter in t:
            str_letter = str(letter)
            if str_letter in t_letter_count.keys():
                t_letter_count[str_letter] += 1
            else:
                t_letter_count[str_letter] = 1

        for letter in s:
            t_letter_count[str(letter)] -= 1
        for letter in t_letter_count.keys():
            if t_letter_count[letter] == 1:
                return letter
        return ""

        # ascii approach
        ascii_sum_s = 0
        ascii_sum_t = 0
        for letter in s:
            ascii_sum_s += ord(letter)
        for letter in t:
            ascii_sum_t += ord(letter)
        return chr(ascii_sum_t - ascii_sum_s) 
        """  
        # bit manipulation approach
        xor = 0
        for letter in s:
            xor = xor ^ ord(letter)
        for letter in t:
            xor = xor ^ ord(letter)
        return chr(xor)