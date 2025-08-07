class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        mi = []
        n=len(nums)
        left = [0]*n;right = [n-1]*n
        for i in range(n):
            while mi and nums[mi[-1]]>=nums[i]:
                mi.pop()
            left[i]= mi[-1]+1 if mi else 0
            mi.append(i)
        mi = []
        for i in range(n-1,-1,-1):
            while mi and nums[mi[-1]]>=nums[i]:
                mi.pop()
            right[i] = mi[-1]-1 if mi else n-1
            mi.append(i)
        ans = 0
        for i in range(n):
            if left[i]<=k<=right[i]:
                score = nums[i] * (right[i]-left[i]+1)
                ans = max(score,ans)
        return ans