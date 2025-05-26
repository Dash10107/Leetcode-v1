class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        @cache
        def func(i):
            if i ==0:
                return 1
            if i ==1:
                return 10
            k = 9
            for j in range(i-1):
                k*= (9-j)
            return k + func(i-1)
        return func(n)