class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0
        for n in nums:
            xor^=n
        return bin(xor ^ k).count('1')