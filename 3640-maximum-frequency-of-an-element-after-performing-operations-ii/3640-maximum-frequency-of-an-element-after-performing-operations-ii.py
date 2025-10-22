class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        ans = 1
        numscounter = Counter(nums)
        nums.sort()
        for i in range(len(nums)):
            ans = max(ans, numscounter[nums[i]])
            ind = bisect_right(nums, nums[i]+2*k)
            ans = max(ans, min(ind-i,numOperations))
            ind = bisect_left(nums, nums[i]-2*k)
            ans = max(ans, min(i-ind+1,numOperations))
            ind1 = bisect_right(nums, nums[i]+k)
            ind2 = bisect_left(nums, nums[i]-k)
            ans = max(ans, min(ind1-i+i-ind2,numOperations+numscounter[nums[i]]))
        return ans
        