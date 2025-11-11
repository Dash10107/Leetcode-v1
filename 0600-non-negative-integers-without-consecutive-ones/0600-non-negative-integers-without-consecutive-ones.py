class Solution:
    def __init__(self):
        self.f=[1,2]
        for i in range(2,30):
            self.f.append(self.f[-1]+self.f[-2])
    def findIntegers(self, n: int) -> int:
        ans = 0;last=0

        for i in reversed(range(30)):
            if (1<<i)&n:
                ans+=self.f[i]
                if last:
                    ans-=1;break
                last=1
            else:last=0
        return ans+1
