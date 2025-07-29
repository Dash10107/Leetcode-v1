class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dist = 0
        for n in nums:
            dist ^=n
        dist = (dist & -dist)
        un1,un2 = 0,0
        for n in nums:
            if n & dist:
                un1 ^= n
            else:
                un2 ^= n
        return [un1,un2]