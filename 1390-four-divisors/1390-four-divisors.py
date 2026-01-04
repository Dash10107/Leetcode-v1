class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def getf(n):
            f = set()
            for i in range(1,int(sqrt(n))+1):
                if n%i==0:
                    f.add(i)
                    f.add(n//i)
            return f
        ans = 0
        for n in nums:
            s = getf(n)
            if len(s)==4:
                ans+=sum(s)
        return ans