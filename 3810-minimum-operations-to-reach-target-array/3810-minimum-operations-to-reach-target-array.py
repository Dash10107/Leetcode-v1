class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        s = set()
        for n,t in zip(nums,target):
            if n!=t:
                s.add(n)
        return len(s)