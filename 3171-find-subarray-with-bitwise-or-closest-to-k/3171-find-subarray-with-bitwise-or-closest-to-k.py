class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prev = set()
        ans = float('inf')
        for num in nums:
            curr = {num}
            ans = min(ans,abs(num-k))
            for c in prev:
                curr.add(c|num)
                ans = min(ans,abs((c|num)-k))
            prev = curr
        return ans