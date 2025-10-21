class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        tree= defaultdict(list)
        for i,j in edges:
            tree[i].append(j)
            tree[j].append(i)
        self.ans=0
        def dfs(node,par):
            s=1;childs=set()
            for j in tree[node]:
                if j==par:continue
                size=dfs(j,node)
                s+=size
                childs.add(size)
            if len(childs)<=1:self.ans+=1
            return s
        s=dfs(0,-1)
        return self.ans