class Solution:
    def minJumps(self, arr: List[int]) -> int:
        same =defaultdict(list)
        n = len(arr)
        for i,a in enumerate(arr):
            same[a].append(i)

        q = deque([0])
        vis = [float('inf')]*n;vis[0]=0
        while q:
            node = q.popleft()
            if node==n-1:return vis[node]
            nexts = []
            if node+1<n:nexts.append(node+1)
            if node-1>=0:nexts.append(node-1)
            if arr[node] in same:
                nexts.extend(same[arr[node]])
                del same[arr[node]]
            for nex in nexts:
                if vis[node]+1<=vis[nex]:
                    vis[nex]=vis[node]+1
                    q.append(nex)
        return vis[n-1]