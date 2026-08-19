class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # pairs = {
        #     ')' : '(',
        #     '}' : '{',
        #     ']' : '['
        # }
        # for ch in s:
        #     if ch in '({[':
        #         stack.append(ch)
        #     else:
        #         if not stack:
        #             return False
        #         if stack[-1] != pairs[ch]:
        #             return False
        #         stack.pop()
        # return len(stack) == 0
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop()!= '(':
                    return False
            elif char == '}':
                if not stack or stack.pop()!= '{':
                    return False
            elif char == ']':
                if not stack or stack.pop()!= '[':
                    return False
        return len(stack)==0
