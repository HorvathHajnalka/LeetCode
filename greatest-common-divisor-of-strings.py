class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        divisor = ""
        idx = 0
        maxlength = 0
        intdivisors = []
        
        if len(str1) > len(str2):
            for i in range(1, len(str1) - len(str2)+1):
                if len(str1) % i == 0 and len(str2) % i == 0:
                    intdivisors.append(i)
            maxlength = intdivisors[-1]
            print(maxlength)
        elif len(str1) < len(str2):
            for i in range(1, len(str2) - len(str1)+1):
                if len(str1) % i == 0 and len(str2) % i == 0:
                    intdivisors.append(i)
            maxlength = intdivisors[-1]
        else:
            maxlength = len(str1)
        while(idx < maxlength):  
            if(str1[idx] != str2[idx]):
                return ""   
            divisor += str1[idx]
            idx+=1
        if divisor == "":
            return ""
        for i in range(0,min(len(str1), len(str2)), len(divisor)):
            if str1[i:i+len(divisor)] != divisor or str2[i:i+len(divisor)] != divisor:
                return ""
        if len(str1) > len(str2):
            for j in range(len(str2), len(str1), len(divisor)):
                if str1[j:j+len(divisor)] != divisor:
                    return ""
        elif len(str2) > len(str1):
            for j in range(len(str1), len(str2), len(divisor)):
                if str2[j:j+len(divisor)] != divisor:
                    return ""
        return divisor