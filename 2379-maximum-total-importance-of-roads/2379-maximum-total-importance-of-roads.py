class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        indegree = [0]*n
        for u,v in roads:
            indegree[u]+=1
            indegree[v]+=1
        indegree.sort(reverse=True)
        ans = 0
        j = n
        for i in indegree:
            ans+= j*i
            j-=1
        return ans
