class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        xor = 0
        for n in nums:
            if n%2==0:
                xor|=n       
        return xor