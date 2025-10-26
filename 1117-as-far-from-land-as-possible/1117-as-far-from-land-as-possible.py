class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirr = [(0,1),(1,0),(-1,0),(0,-1)]
        q = deque([(i,j) for i in range(n) for j in range(m) if grid[i][j] == 1])
        if not q or len(q) == n * m: return -1
        ans = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                i, j = q.popleft()
                for dr, dc in dirr:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr, nc))
            ans += 1
        return ans - 1
