class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10**9+7
        def dfs(arr):
            n = len(arr)
            if n<=2:return 1
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            ln, rn = len(left), len(right)    
            c = comb(n-1,ln)
            ans = ((c*dfs(left))%mod * dfs(right))%mod
            return ans
        return (dfs(nums)-1)%mod