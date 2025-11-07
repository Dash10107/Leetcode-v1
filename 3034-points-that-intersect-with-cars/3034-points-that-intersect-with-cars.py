class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        arr=[0]*(101)
        for s,e in nums:
            for i in range(s,e+1):
                arr[i]+=1
        return 101-arr.count(0)