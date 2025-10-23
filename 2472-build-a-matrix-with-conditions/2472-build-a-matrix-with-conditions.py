from collections import defaultdict, deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topos(graph):
            indeg = [0]*(k+1)
            for u in range(1, k+1):
                for v in graph[u]:
                    indeg[v] += 1
            q = deque([u for u in range(1, k+1) if indeg[u] == 0])
            topo = []
            while q:
                u = q.popleft()
                topo.append(u)
                for v in graph[u]:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)
            return topo if len(topo) == k else []

        g1 = defaultdict(list)
        g2 = defaultdict(list)
        for a, b in rowConditions:
            g1[a].append(b)
        for a, b in colConditions:
            g2[a].append(b)

        rtopo = topos(g1)
        ctopo = topos(g2)
        if not rtopo or not ctopo:
            return []

        rowPos = {num: i for i, num in enumerate(rtopo)}
        colPos = {num: j for j, num in enumerate(ctopo)}

        mat = [[0]*k for _ in range(k)]
        for num in range(1, k+1):
            r, c = rowPos[num], colPos[num]
            mat[r][c] = num
        return mat
