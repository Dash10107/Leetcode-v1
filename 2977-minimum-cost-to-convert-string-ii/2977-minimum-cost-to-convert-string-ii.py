class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        mod = 1<<32
        base = 27
        mask = (1<<32)-1 
        INF = 10**10
        def hash(s):
            H = 0
            m = len(s)
            for i in range(m):
                ch = ord(s[i])-96
                H = (H * base + ch) & mask
            return H
            
        graph = {hash(chr(i+97)):{hash(chr(i+97)):0} for i in range(26)}
        all_items = set()
        for i in range(len(cost)):
            u = hash(original[i])
            v = hash(changed[i])
            all_items.add(u);all_items.add(v)
            graph.setdefault(u, {})
            graph[u][v] = min(graph[u].get(v, INF), cost[i])

        graph_keys = list(graph.keys())
        all_items = list(all_items)
        for k in all_items:
            if k not in graph: continue
            for i in graph_keys:
                if k not in graph[i]: continue
                for j in graph[k]:
                    if j in graph[i]:
                        graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
                    else:
                        graph[i][j] = graph[i][k]+graph[k][j]

        n = len(source)
        powB = [1] * (n + 1)
        for i in range(1, n + 1):
            powB[i] = (powB[i - 1] * base) & mask
        ps = [0] * (n + 1) # prefix_hash_source
        pt = [0] * (n + 1) # prefix_hash_target
        for i in range(1, n + 1):
            ps[i] = (ps[i - 1] * base + (ord(source[i - 1]) - 96)) & mask
            pt[i] = (pt[i - 1] * base + (ord(target[i - 1]) - 96)) & mask
        def subhash(p, l, r):
            L = r - l
            return (p[r] - p[l] * powB[L]) & mask

        dp = [INF]*(n+1)
        dp[0] = 0
        lens = sorted({len(s) for s in original} | {1})
        for j in range(1, n + 1):
            for L in lens:
                i = j - L
                if i < 0:
                    break
                u = subhash(ps, i, j)
                v = subhash(pt, i, j)
                if u == v:
                    dp[j] = min(dp[j], dp[i])
                elif u in graph and v in graph[u]:
                    dp[j] = min(dp[j], dp[i] + graph[u][v])

        return dp[n] if dp[n] != INF else -1