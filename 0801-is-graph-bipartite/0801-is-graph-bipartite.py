from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)
        def dfs(node,col):
            color[node]=col
            for neg in graph[node]:
                if color[neg]==-1:
                    if not dfs(neg,1-col):return False
                elif color[neg]==color[node]:
                    return False
            return True
        for start in range(len(graph)):
            if color[start] == -1:
                if not dfs(start,0):
                    return False
        return True
