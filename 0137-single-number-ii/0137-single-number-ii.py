class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            s = 0
            for n in nums:
                if (n>>i)&1:
                    s = (s+1)%3
            if s!=0:ans |= s<<i
        if ans >= 2**31:
            ans -= 2**32
        return ans