class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans =0;prev=float('-inf')
        for n  in nums:
            low=n-k;high=n+k
            if prev<low:
                prev=low
                ans+=1
            elif prev<high:
                prev+=1
                ans+=1
        return ans