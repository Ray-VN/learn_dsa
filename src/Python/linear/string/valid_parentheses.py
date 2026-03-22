class Solution(object):
    def isValid(self, s):
        stack = []
        for i, item in enumerate(s):
            
            if item in ('(', '[', '{'):
                stack.append(item)
            elif len(stack) > 0 and item in (')', ']', '}'):
                if item == ')' and stack[-1] == '(':
                    stack.pop()
                elif item == ']' and stack[-1] == '[':
                    stack.pop()
                elif item == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                return False
            
        if len(stack) == 0:
            return True
        else:
            return False

s = "]"
so = Solution()
print(so.isValid(s))

