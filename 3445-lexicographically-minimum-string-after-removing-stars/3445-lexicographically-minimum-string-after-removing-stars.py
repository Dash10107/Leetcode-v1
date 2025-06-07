class Solution:
    def clearStars(self, s: str) -> str:
        q = []
        ans = []
        for i in range(len(s)):
            if s[i]=='*':
                if q:
                    _,ind =  heapq.heappop(q)
                    ans[-ind]=''
            else:
                heapq.heappush(q,(s[i],-len(ans)))
                ans.append(s[i])
        return ''.join(ans)