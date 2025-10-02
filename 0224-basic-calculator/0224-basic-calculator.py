class Solution:
    def calculate(self, s: str) -> int:
        output, cur, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c in "+-":
                output += cur * sign
                cur = 0
                sign = -1 if c == '-' else 1
            elif c == "(":
                stack.append(output)
                stack.append(sign)
                output, sign = 0, 1
            elif c == ")":
                output += cur * sign
                output *= stack.pop()
                output += stack.pop()
                cur = 0
        return output + cur * sign