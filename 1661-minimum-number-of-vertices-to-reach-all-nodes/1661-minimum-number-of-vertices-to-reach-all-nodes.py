class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indeg = [0]*n
        for u,v in edges:
            indeg[v]+=1
        ans=[i for i,deg in enumerate(indeg) if deg==0]
        return ans
