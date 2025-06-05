class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        c = {0:1}
        ans = 0
        curr = 0
        for num in nums:
            curr+=num
            if curr-goal in c:
                ans+= c[curr-goal]
            c[curr]= c.get(curr,0)+1
        
        return ans