class Solution(object):
    def titleToNumber(self, columnTitle):
        i = 0
        columnNumber = 0
        for letter in columnTitle[::-1]:
            columnNumber += (ord(letter)-64)*pow(26,i)
            i += 1
        return columnNumber