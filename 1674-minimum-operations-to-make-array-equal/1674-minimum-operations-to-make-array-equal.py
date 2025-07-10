class Solution:
    def minOperations(self, n: int) -> int:
        arr = [(2 * i + 1) for i in range(n)]
        t = (arr[0]+arr[-1])//2
        ans = 0
        for i in range(n):
            if arr[i]>=t:
                break
            ans+= (t-arr[i])
        return ans