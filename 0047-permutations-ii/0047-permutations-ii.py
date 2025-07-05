class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for perm in permutations(nums):
            ans.add(perm)
        return list(ans)