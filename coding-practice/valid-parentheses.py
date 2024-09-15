class Solution(object):
    def isValid(self, s):
        pairs ={
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        stack = []
        for ch in s:
            if ch in pairs:
                stack.append(ch)
            else:
                if len(stack) == 0 or pairs[stack.pop()] != ch:
                    return False
        if len(stack) != 0:
            return False
        return True