class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums);m = max(c.values())
        ans = 0
        for ch in c:
            if c[ch]==m:ans+=c[ch]
        return ans