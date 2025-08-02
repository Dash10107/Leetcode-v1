class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        ans = float('inf')
        n = len(mat);m = len(mat[0])
        dirr = [(0,1),(1,0),(-1,0),(0,-1)]
        q  = deque([mat])
        vis = set();step =0
        def flip(res,i,j):
            node = deepcopy(res)
            node[i][j] = 1 - node[i][j]
            for dr,dc in dirr:
                nr,nc = i+dr,j+dc
                if 0<=nr<n and 0<=nc<m:
                    node[nr][nc]= 1-node[nr][nc]
            return node
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if sum(map(sum,node))==0:
                    return step
                for i in range(n):
                    for j in range(m):
                        newNode = flip(node,i,j)
                        hashNode = tuple(map(tuple,newNode))
                        if hashNode in vis:
                            continue
                        vis.add(hashNode)
                        q.append(newNode)
            step+=1
        return -1