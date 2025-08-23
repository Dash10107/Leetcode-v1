class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        map = defaultdict(int)

        def get_one(i1, j1, i2, j2):
            minx = float('inf')
            maxx = float('-inf')
            miny = float('inf')
            maxy = float('-inf')

            for i in range(i1, i2 + 1):
                for j in range(j1, j2 + 1):
                    if grid[i][j] == 1:
                        minx = min(minx, i)
                        maxx = max(maxx, i)
                        miny = min(miny, j)
                        maxy = max(maxy, j)

            if minx == float('inf'):
                return 0

            return (maxx - minx + 1) * (maxy - miny + 1)

        def get_next(i1, j1, i2, j2, k):
            key = (i1, j1, i2, j2, k)
            if key in map:
                return map[key]

            output = float('inf')

            if k == 1:
                output = get_one(i1, j1, i2, j2)
            elif k == 2:
                for i in range(i1, i2):
                    output = min(output, get_next(i1, j1, i, j2, 1) + get_next(i + 1, j1, i2, j2, 1))
                for j in range(j1, j2):
                    output = min(output, get_next(i1, j1, i2, j, 1) + get_next(i1, j + 1, i2, j2, 1))
            elif k == 3:
                for i in range(i1, i2):
                    output = min(output, get_next(i1, j1, i, j2, 1) + get_next(i + 1, j1, i2, j2, 2))
                    output = min(output, get_next(i1, j1, i, j2, 2) + get_next(i + 1, j1, i2, j2, 1))
                for j in range(j1, j2):
                    output = min(output, get_next(i1, j1, i2, j, 1) + get_next(i1, j + 1, i2, j2, 2))
                    output = min(output, get_next(i1, j1, i2, j, 2) + get_next(i1, j + 1, i2, j2, 1))

            map[key] = output
            return output

        m = len(grid)
        n = len(grid[0])

        ans = get_next(0, 0, m - 1, n - 1, 3)

        return ans