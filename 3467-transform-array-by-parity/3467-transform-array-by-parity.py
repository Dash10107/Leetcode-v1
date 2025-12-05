class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        zer,one=0,0
        for n in nums:
            if n&1:one+=1
            else:zer+=1
        return( [0]*zer + [1]*one)