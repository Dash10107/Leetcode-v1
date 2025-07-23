class Solution:
    def maximumInvitations(self, favorite):
        n = len(favorite)
        indegree = [0]*n;depth=[1]*n
        lcycle = 0;twoCycle=0
        for i,f in enumerate(favorite):
            indegree[f]+=1
        q = deque()
        for p in range(n):
            if indegree[p]==0:
                q.append(p)
        while q:
            node = q.popleft()
            nt = favorite[node]
            depth[nt]=max(depth[node]+1,depth[nt])
            indegree[nt]-=1
            if indegree[nt]==0:
                q.append(nt)
        for p in range(n):
            if indegree[p]==0:continue
            l=0;curr = p
            while indegree[curr]:
                indegree[curr]=0
                l+=1
                curr = favorite[curr]
            if l==2:
                twoCycle+= depth[curr] + depth[favorite[curr]]
            else:
                lcycle = max(lcycle,l)
        return max(lcycle,twoCycle)