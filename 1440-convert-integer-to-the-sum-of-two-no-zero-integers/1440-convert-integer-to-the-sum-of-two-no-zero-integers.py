class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def check(s):
            return ('0' in str(s))
        for i in range(1,n):
            if not check(i) and not check(n-i):
                return [i,n-i]