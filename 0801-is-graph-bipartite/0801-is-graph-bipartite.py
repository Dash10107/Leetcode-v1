class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)

        for start in range(len(graph)):
            if color[start]!=0:continue
            q= deque([start])
            color[start]=1
            while q:
                node = q.popleft()
                for neg in graph[node]:
                    if color[neg]==0:
                        color[neg]=-color[node]
                        q.append(neg)
                    elif color[neg]!= -color[node]:
                        return False
        return True
                

        return True
