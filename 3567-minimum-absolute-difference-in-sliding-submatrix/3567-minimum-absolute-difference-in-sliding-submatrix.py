class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = []
        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                vals = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.append(grid[x][y])
                vals.sort()
                diff = float('inf')
                for z in range(1, len(vals)):
                    if vals[z] != vals[z - 1]:
                        diff = min(diff, abs(vals[z] - vals[z - 1]))
                row.append(0 if diff == float('inf') else diff)
            ans.append(row)
        return ans