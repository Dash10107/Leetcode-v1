class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indeg = [0]*(n+1)
        graph = defaultdict(list)
        for u,v in relations:
            indeg[v]+=1
            graph[u].append(v)
        finish = [0] * (n + 1)
        q = deque([])
        for i,deg in enumerate(indeg):
            if i==0:continue
            if deg==0:
                q.append(i);finish[i]=time[i-1]
        while q:
            curr = q.popleft()
            for neg in graph[curr]:
                indeg[neg]-=1
                finish[neg]=max(finish[neg],finish[curr]+time[neg-1])
                if indeg[neg]==0:
                    q.append(neg)
        return max(finish)