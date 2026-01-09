class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        def enough(mid):
            c,i,j=0,0,0
            while i<n or j<n:
                while j<n and (nums[j]-nums[i]) <=mid:
                    j+=1
                c+= (j-i-1)
                i+=1
            return c>=k
        left, right = 0, nums[-1]-nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left 