class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        graph = defaultdict(list)
        for s in allowed:
            graph[s[:2]].append(s[2])
        pyr = [['']*(i+1) for i in range(len(bottom))]
        pyr[-1]= [c for c in bottom]

        def func(i,j):
            if i<=0:return True
            if i<=j:return func(i-1,0)
            key = pyr[i][j]+pyr[i][j+1]
            for v in graph[key]:
                pyr[i-1][j]=v
                if func(i,j+1):
                    return True
            return False
        return func(len(pyr)-1,0)