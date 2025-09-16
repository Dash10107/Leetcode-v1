from math import gcd
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            curr = num
            while stack:
                g = gcd(stack[-1], curr)
                if g == 1:
                    break
                curr = stack[-1] * curr // g
                stack.pop()
            stack.append(curr)
        return stack