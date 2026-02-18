class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        ones = s.count('1')
        zero = n-ones
        if abs(ones-zero)>1:
            return -1
        def func(ch):
            ans = 0
            for c in s:
                if c!=ch:
                    ans+=1
                ch = str(1-int(ch))
            return ans//2
        if ones==zero:
            return min(func('0'),func('1'))
        elif ones>zero:
            return func('1')
        else:
            return func('0')