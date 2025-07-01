class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n,m = len(grid),len(grid[0])
        vis = set()
        dic = {}
        dirr = [(0,1),(1,0),(-1,0),(0,-1)]
        q =deque()
        keys = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='@':
                    q.append((i,j,0,0))
                    vis.add((i,j,0))
                elif grid[i][j].islower():
                    keys |= (1 << (ord(grid[i][j]) - ord('a')))
        while q:
            ii,jj,mask,level= q.popleft()
            for dr,dc in dirr:
                nr,nc = ii+dr,jj+dc
                if 0<=nr<n and 0<=nc<m:
                    new = mask
                    if grid[nr][nc]=='#':
                        continue
                    elif grid[nr][nc].islower():
                        new |= (1 << (ord(grid[nr][nc]) - ord('a')))
                        if new==keys:
                            return level+1
                    elif grid[nr][nc].isupper():
                        if not (mask & (1 << (ord(grid[nr][nc].lower()) - ord('a')))):
                            continue
                    if (nr,nc,new ) not in vis:
                        vis.add((nr,nc,new))
                        q.append((nr,nc,new,level+1))


        return -1