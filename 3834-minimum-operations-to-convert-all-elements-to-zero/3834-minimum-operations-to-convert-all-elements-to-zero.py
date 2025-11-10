class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = []
        ans = 0
        for a in nums:
            while s and s[-1]>a:
                s.pop()
            if a==0:continue
            if not s or s[-1]<a:
                ans+=1
                s.append(a)
        return ans