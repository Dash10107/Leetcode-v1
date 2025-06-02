class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow = 0
        fast = 0
        ans = float('inf')
        s = nums[0]
        while fast<len(nums):
            if s<target:
                fast+=1
                if fast<len(nums):
                    s+=nums[fast]
            else:
                ans = min(ans,fast-slow+1)
                s-=nums[slow]
                slow+=1
        return ans if ans!=float('inf') else 0