class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
            xor_arr = 0
            for num in nums:
                xor_arr |=num
            count = [0]
            self.findSubsets(nums,0,0,xor_arr,count)
            return count[0]             
    
    def findSubsets(self,nums,i,subans,ans,count):
        if ans == subans:
            count[0]+=1
        for i in range(i,len(nums)):
            self.findSubsets(nums,i+1,subans | nums[i],ans,count)
        