class Solution:
    def minCost(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def func(i,j):
            if j>=n:return i
            if j+1>=n:return max(i,nums[j])
            arr = [nums[j],i,nums[j+1]]
            arr.sort()
            a = max(arr[1],arr[2])+ func(arr[0],j+2)
            b = max(arr[0],arr[1])+func(arr[2],j+2)
            c = max(arr[0],arr[2])+func(arr[1],j+2)
            return min(a,b,c)
        return func(nums[0],1)