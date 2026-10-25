class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in parentheses:
                top_element = stack.pop() if stack else ""
                if top_element != parentheses[char]:
                    return False

            else:
                stack.append(char)

        return not stack