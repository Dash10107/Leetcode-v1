class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = []
        for ch in c:
            if c[ch]==1:
                ans.append(ch)
        return ans