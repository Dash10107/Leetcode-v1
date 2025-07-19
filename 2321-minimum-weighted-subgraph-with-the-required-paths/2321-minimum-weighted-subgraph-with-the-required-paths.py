class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        g1 = defaultdict(list);g2 = defaultdict(list)
        for u,v,w in edges:
            g1[u].append((w,v))
            g2[v].append((w,u))
        def func(src,g):
            vis = [float('inf')]*n
            vis[src]=0
            heap = []
            heappush(heap,(0,src))
            while heap:
                w,s = heappop(heap)
                if w>vis[s]:continue
                for cost,node in g[s]:
                    if w+cost<vis[node]:
                        vis[node]=w+cost
                        heappush(heap,(vis[node],node))
            return vis
        l1,l2,l3 = func(src1,g1),func(src2,g1),func(dest,g2)
        ans  = float('inf')
        for i in range(n):
            ans = min(ans,l1[i]+l2[i]+l3[i])
        return ans if ans!=float('inf') else -1
