class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], ss:int) -> List[int]:
        n = len(edges)+1
        cnt = 0
        graph = defaultdict(list)
        def dfs(node,par,d):
            nonlocal cnt
            if d%ss==0:cnt+=1
            for ch,dis in graph[node]:
                if ch!=par:dfs(ch,node,d+dis)
            return
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
        res = [0]*n
        for i in range(n):
            ans,s = 0,0
            temp = []
            for ch,w in graph[i]:
                cnt = 0
                dfs(ch,i,w)
                temp.append(cnt)
                s+=cnt
            for el in temp:ans+= (s-el)*el 
            res[i]=ans//2
        return res