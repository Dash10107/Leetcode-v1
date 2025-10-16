class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        vals = list(range(value))
        for val in nums:
            j = val%value
            if j<0:
                vals[j+value]+=1
            else:
                vals[j]+=value
        return min(vals)