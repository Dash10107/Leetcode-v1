class Solution:
    def maxSubarrayLength(self, arr: List[int], k: int) -> int:
        ans = 0
        n = len(arr)
        c=defaultdict(int)
        j = 0
        for i in range(n):
            c[arr[i]]+=1
            while c[arr[i]]>k:
                c[arr[j]]-=1
                j+=1
            ans=max(ans,i-j+1)
        return ans