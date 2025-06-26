class Solution:
    def restoreArray(self, pairs: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for u,v in pairs:
            g[u].append(v)
            g[v].append(u)
        ans = []
        for node in g:
            if len(g[node])==1:
                ans.append(node)
                ans.append(g[node][0])
                break
        while len(ans)<len(g):
            last,slast = ans[-1],ans[-2]
            neg = g[last]
            if neg[0]!=slast:
                ans.append(neg[0])
            else:
                ans.append(neg[1])
        return ans