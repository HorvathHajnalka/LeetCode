class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = []
        s.append(chars[0])
        i = 1
        j = 0
        s_size = 1
        while i != len(chars):
            if chars[i] == s[j]:
                s.append(2)
                i += 1
                j += 1
                s_size += 1
            elif type(s[j]) == int and s[j-1] == chars[i]:
                s[j] += 1
                i += 1
                if s[j] == 10 or s[j] == 100 or s[j] == 1000:
                    s_size += 1
            elif type(s[j]) == int and s[j-1] != chars[i]:
                s.append(chars[i])
                i += 1
                j += 1
                s_size += 1
            elif type(s[j]) == unicode and s[j] != chars[i]:
                s.append(chars[i])
                i += 1
                j += 1
                s_size += 1
        print(s)
        i = 0
        for k in range(0, len(s)):
            if type(s[k]) == int:
                dividend = s[k]
                remains = []
                while(dividend != 0):
                    remains.append(dividend % 10)
                    dividend //= 10
                for j in range(len(remains)-1, -1, -1):
                    print(j, remains)
                    chars[i] = str(remains[j])
                    i += 1
                    print(chars)
            else:
                chars[i] = str(s[k])
                i += 1
        return s_size