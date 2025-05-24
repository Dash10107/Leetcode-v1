class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        freq = [0]*len(nums)
        def func(arr,freq):
            if len(arr)==len(nums):
                ans.append(arr[:])
                return
            for i in range(len(nums)):
                if not freq[i]:
                    freq[i]=1
                    func(arr+[nums[i]],freq)
                    freq[i]=0
        func([],freq)
        return ans