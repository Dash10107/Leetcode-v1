class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        def dfs(start):
            dist = [-1]*n
            vis = [False]*n
            d= 0
            curr = start
            while curr!=-1 and not vis[curr]:
                dist[curr]=d
                vis[curr]=True
                d+=1
                curr = edges[curr]
            return dist
        dist1 = dfs(node1)
        dist2 = dfs(node2)
        ans = -1
        mdist = float('inf')
        for i in range(n):
            if dist1[i]!=-1 and dist2[i]!=-1:
                temp = max(dist1[i],dist2[i])
                if temp<mdist:
                    mdist = temp
                    ans = i
        return ans
            