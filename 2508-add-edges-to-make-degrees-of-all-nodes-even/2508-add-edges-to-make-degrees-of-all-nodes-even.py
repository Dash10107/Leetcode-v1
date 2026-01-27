class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        degree = [0]*(n)
        graph = defaultdict(set)
        for u,v in edges:
            degree[u-1]+=1
            degree[v-1]+=1
            graph[u-1].add(v-1)
            graph[v-1].add(u-1)
        odd = [ i for i,deg in enumerate(degree) if deg&1]
        if len(odd)==0:
            return True
        if len(odd)==2:
            u,v = odd
            if v not in graph[u]:return True
            for i in range(n):
                if i!=u and i!=v and i not in graph[u] and i not in graph[v]:
                    return True
            return False
        if len(odd)==4:
            a,b,c,d = odd
            pairs = [(a,b,c,d),(a,c,b,d),(a,d,b,c)]
            for x1,x2,y1,y2 in pairs:
                if x2 not in graph[x1] and y2 not in graph[y1]:
                    return True
            return False
        return False

        