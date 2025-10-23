class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q = deque([(0,[0])])
        n = len(graph)
        ans = []
        while q:
            node,path=q.popleft()
            if node==n-1:
                ans.append(path)
            for neg in graph[node]:
                q.append((neg,path+[neg]))
        return ans