class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] in [")", "]", "}"]:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if s[i] == "(":
                    if stack[-1] != ")":
                        return False
                    else:
                        stack.pop(len(stack) - 1)
                elif s[i] == "[":
                    if stack[-1] != "]":
                        return False
                    else:
                        stack.pop(len(stack) - 1)
                elif s[i] == "{":
                    if stack[-1] != "}":
                        return False
                    else:
                        stack.pop(len(stack) - 1)
        return len(stack) == 0
