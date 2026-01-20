class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            flag = True
            for j in range(2,nums[i]+1):
                if j|j-1 == nums[i]:
                    ans.append(j-1)
                    flag = False
                    break
            if flag:
                ans.append(-1) 
            
        return ans