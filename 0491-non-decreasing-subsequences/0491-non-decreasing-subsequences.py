class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def func(ind,temp):
            if ind==len(nums):
                if len(temp) >= 2:
                    ans.add(tuple(temp))
                return
            if not temp or nums[ind]>=temp[-1]:
                func(ind+1,temp+[nums[ind]])
            func(ind + 1, temp)
        func(0,[])
        return [list(seq) for seq in ans]