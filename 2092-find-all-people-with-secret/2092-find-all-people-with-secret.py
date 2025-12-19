class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], first: int) -> List[int]:
        dist = [float('inf')]*n
        dist[0]=0;dist[first]=0
        graph = defaultdict(list)
        graph[0].append((first,0))
        for x,y,t in meetings:
            graph[x].append((y,t))
            graph[y].append((x,t))
        heap = [(0,0),(0,first)]
        while heap:
            time,node = heappop(heap)
            if time>dist[node]:continue
            for neg,t in graph[node]:
                if time<=t and t<dist[neg]:
                    dist[neg]=t
                    heappush(heap,(t,neg))
        return [i for i in range(n) if dist[i]!=float('inf')]