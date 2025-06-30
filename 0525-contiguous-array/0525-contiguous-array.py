class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        p = 0
        m = {0:-1}
        ans = 0
        for i,n in enumerate(nums):
            p+=1 if n else -1
            if p in m:
                ans = max(ans,i-m[p])
            else:
                m[p]=i
        return ans