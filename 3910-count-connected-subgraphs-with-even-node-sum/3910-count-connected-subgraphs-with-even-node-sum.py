class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        n=len(nums)
        graph = defaultdict(list)
        for [a,b] in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(mask,v,vi):
            vi[v]=True
            s=nums[v]
            for u in graph[v]:
                if not vi[u] and mask &(1<<u):
                    s+=dfs(mask,u,vi)
            return s
        def help(mask,v):
            vi=[False]*n
            s = dfs(mask,v,vi)
            for i in range(n):
                if (mask & (1<<i))>0 and not vi[i]:
                    return False
            return s%2==0
        ans=0
        for mask in range(1,1<<n):
            for i in range(n):
                if mask & (1<<i):
                    if (help(mask,i)):
                        ans+=1
                        break
        return ans 