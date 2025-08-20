class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g = defaultdict(list)
        for (a,b),p in zip(edges,succProb):
            g[a].append((b,p))
            g[b].append((a,p))
        prob = [0.0]*n
        prob[start]=1.0
        heap = [(-1.0,start)]
        while heap:
            pro,node = heappop(heap)
            for neg,edgep in g[node]:
                if prob[neg] < (-pro)*edgep:
                    prob[neg] = (-pro)*edgep
                    heappush(heap,(-prob[neg],neg))
        return prob[end]