class Solution:
    def isValid(self, s: str) -> bool:

        valid = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                valid.append(char)
            elif len(valid) > 0 and (
                (char == ')' and valid[-1] == '(') or
                (char == '}' and valid[-1] == '{') or
                (char == ']' and valid[-1] == '[')
            ):
                valid.pop()
            else:
                return False

        return len(valid) == 0