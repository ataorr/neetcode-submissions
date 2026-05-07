class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif stack == [] or stack.pop() != closeToOpen[c]:
                return False
        return stack == []
                