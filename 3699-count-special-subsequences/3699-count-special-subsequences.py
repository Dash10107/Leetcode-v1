class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        freq = Counter()
        ans = 0 
        for i in range(n): 
            for j in range(i-3): 
                freq[nums[i-2]/nums[j]] += 1
            for j in range(i+2, n): 
                ans += freq[nums[i]/nums[j]]
        return ans 