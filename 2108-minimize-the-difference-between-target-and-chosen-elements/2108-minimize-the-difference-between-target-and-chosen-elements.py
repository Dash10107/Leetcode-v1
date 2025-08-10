class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        p = 1
        for row in mat:
            tmp =0
            for c in row:
                tmp |= (p<<c)
            p = tmp
        ans = 10**9
        for s in range(5000):
            if (p>>s)&1:
                ans = min(ans,abs(s-target))
        return ans