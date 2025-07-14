class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        n = len(nums)
        def func(temp,ind):
            if ind==n:
                ans.append(temp)
                temp = []
                return
            func(temp,ind+1)
            func(temp+[nums[ind]],ind+1)
        func([],0)
        return ans