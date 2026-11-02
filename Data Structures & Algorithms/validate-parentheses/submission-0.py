class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_dict = {")" : "(", "]": "[", "}": "{"}
        for bracket in s:
            if bracket in bracket_dict:
                if stack and (stack[-1] == bracket_dict[bracket]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return True if not stack else False