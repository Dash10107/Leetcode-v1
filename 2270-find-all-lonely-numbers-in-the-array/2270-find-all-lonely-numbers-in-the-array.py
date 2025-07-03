class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = []
        for n in nums:
            if c[n]==1 and n-1 not in c and n+1 not in c:
                ans.append(n)
        return ans