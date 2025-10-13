class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        ans = 0
        for ch in c:
            if c[ch]%k==0:
                ans+=(ch*c[ch])
        return ans