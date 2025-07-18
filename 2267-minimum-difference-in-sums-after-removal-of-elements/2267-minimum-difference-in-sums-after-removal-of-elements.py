class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n3 = len(nums)
        n = n3//3
        h1 = [];h2 = []
        left = 0;right=0
        lm = [0]*n3;rm = [0]*n3
        for i in range(n3):
            heappush(h1,-nums[i])
            left+=nums[i]
            if len(h1)>n:
                left+= heappop(h1)
            if i>=n-1:
                lm[i]=left
        for i in range(n3-1,-1,-1):
            heappush(h2,nums[i])
            right+=nums[i]
            if len(h2)>n:
                right-= heappop(h2)
            if i<=n3-n:
                rm[i]=right
        res = float('inf')
        for i in range(n-1,n3-n):
            res = min(res,lm[i]-rm[i+1])
        return res