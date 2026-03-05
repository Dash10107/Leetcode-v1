class Solution:
    def minOperations(self, s: str) -> int:
        def func(st):
            ans=0
            for i,ch in enumerate(s):
                if ch!=st:
                    ans+=1
                st = '1' if st=='0' else '0'
            return ans
        return min(func('1'),func('0'))

