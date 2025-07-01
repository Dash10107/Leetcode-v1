class DSU:
    def __init__(self, n):
        """
        Initializes the DSU structure.
        parent[i] stores the parent of element i.
        rank[i] stores the rank of the set represented by i (for union by rank).
        """
        self.parent = list(range(n))
        self.rank = [0] * n  # For union by rank optimization
        # self.size = [1] * n # Alternative for union by size optimization

    def find(self, i):
        """
        Finds the representative (root) of the set containing element i.
        Applies path compression for optimization.
        """
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]

    def union(self, i, j):
        """
        Unites the sets containing elements i and j.
        Applies union by rank optimization.
        Returns True if a union occurred, False if i and j were already in the same set.
        """
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union by rank: attach smaller rank tree under the root of the larger rank tree
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_j] < self.rank[root_i]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        a = DSU(n+1)
        b = DSU(n+1)
        ans = 0
        ae,be = 0,0
        edges.sort(key=lambda x:x[0],reverse=True)
        for t,u,v in edges:
            if t==3:
                if a.union(u,v):
                    b.union(u,v)
                    ae+=1
                    be+=1
                else:ans+=1
            elif t==2:
                if b.union(u,v):
                    be+=1
                else:ans+=1
            elif t==1:
                if a.union(u,v):
                    ae+=1
                else:
                    ans+=1
        if ae==n-1 and be==n-1:
            return ans
        else:
            return -1
            
        