class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n=len(words)
        overlap = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i==j:continue
                m = min(len(words[i]),len(words[j]))
                for k in range(m,-1,-1):
                    if words[i].endswith(words[j][:k]):
                        overlap[i][j]=k
                        break
        dp = [[0]*n for i in range(1<<n)]
        par = [[-1]*n for i in range(1<<n)]
        for mask in range(1<<n):
            for i in range(n):
                if not (mask & (1<<i)):continue
                prev = mask^(1<<i)
                if prev==0:
                    dp[mask][i]=len(words[i])
                    continue
                dp[mask][i]=float('inf')
                for j in range(n):
                    if prev & (1<<j):
                        val=dp[prev][j]+len(words[i])-overlap[j][i]
                        if val<dp[mask][i]:
                            dp[mask][i]=val
                            par[mask][i]=j
        mask = (1<<n) - 1
        last = min(range(n), key=lambda i: dp[mask][i])
        path = []
        while last != -1:
            path.append(last)
            temp = par[mask][last]
            mask ^= (1<<last)
            last = temp

        path = path[::-1]

        res = words[path[0]]

        for i in range(1, len(path)):
            o = overlap[path[i-1]][path[i]]
            res += words[path[i]][o:]

        return res
                