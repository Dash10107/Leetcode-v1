class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        self.ans = float('inf')
        sums = [0]*k
        def dfs(i):
            if i==n:
                self.ans = min(self.ans,max(sums))
                return
            for j in range(k):
                sums[j]+=cookies[i]
                if max(sums)<self.ans:
                    dfs(i+1)
                sums[j]-=cookies[i]
                if sums[j]==0:break
        dfs(0)
        return self.ans
