class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        ans = 0
        arr = []
        for g in grid:
            for num in g:
                if (num-grid[0][0])%x==0:
                    arr.append(num)
                else:
                    return -1
        arr.sort()
        mid = arr[len(arr)//2]
        for i in range(len(arr)):
                ans+= abs(mid-arr[i])//x
        return ans