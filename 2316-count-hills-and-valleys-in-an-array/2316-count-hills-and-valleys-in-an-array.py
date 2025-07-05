class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        curr = 0
        n = len(nums)
        for i in range(n):
            if nums[i]==curr:
                continue
            curr = nums[i]
            back,front = curr,curr
            j = i
            while j>=0 and nums[j]==curr:
                    j-=1
            if j>=0:
                back = nums[j]
            j  = i
            while j<n and nums[j]==curr:
                    j+=1
            if j<n:
                front = nums[j]
            if back<curr and front<curr:
                ans+=1
            elif back>curr and front>curr:
                ans+=1
        return ans
                