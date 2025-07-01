class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        graph = defaultdict(set)
        for i,route in enumerate(routes):
            for r in route:
                graph[r].add(i)
        q = deque([(source,0)])
        vis = set()
        vis.add(source)
        visr = set()
        while q:
            node,level = q.popleft()
            for b in graph[node]:
                if b in visr:
                    continue
                visr.add(b)
                for r in routes[b]:
                    if r ==target:
                        return level+1
                    if r not in vis:
                        vis.add(r)
                        q.append((r,level+1))

        return -1