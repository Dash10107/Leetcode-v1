class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        par = [-1]*n
        for i in range(n):
            if leftChild[i]!=-1:                
                if  par[leftChild[i]]==-1:
                    par[leftChild[i]]=i
                else:return False
            if rightChild[i]!=-1:
                if par[rightChild[i]]==-1:
                    par[rightChild[i]]=i
                else:return False
        if par.count(-1)!=1:return False
        root = par.index(-1)
        vis = set()
        def dfs(u):
            if u==-1:return True
            if u in vis:return False
            vis.add(u)
            return dfs(leftChild[u]) and dfs(rightChild[u])
        return dfs(root) and len(vis)==n
