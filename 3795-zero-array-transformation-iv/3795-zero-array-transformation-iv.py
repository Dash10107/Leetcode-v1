class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        @cache
        def dfs(val, k, i):
            if val == 0:
                return True
            
            if k < 0 or val < 0:
                return False

            l = False
            if queries[k][0] <= i <= queries[k][1]:
                l = dfs(val - queries[k][2], k-1, i)
            r = dfs(val, k - 1, i)

            return l or r
        
        def check(k):
            for i in range(len(nums)):
                if not dfs(nums[i], k - 1, i):
                    return False

            return True
        
        l, r = 0, len(queries)
        ans = -1
        
        while l <= r:
            m = (l + r) // 2
            
            if check(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans