class Solution:
    def countSubarrays(self, arr: List[int], k: int) -> int:
        ans = 0
        n = len(arr)
        m = max(arr)
        mc = 0
        j = 0
        for i in range(n):
            if arr[i]==m:
                mc+=1
            while mc>=k:
                if arr[j]==m:
                    mc-=1
                j+=1
            ans +=j
        return ans