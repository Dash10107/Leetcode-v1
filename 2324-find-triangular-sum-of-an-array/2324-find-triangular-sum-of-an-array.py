class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        i = 0;n=len(nums)
        while i<n:
            prev= nums[i]
            for j in range(i+1,n):
                temp = nums[j]
                nums[j]= (nums[j]+prev)%10
                prev= temp
            i+=1
        return nums[-1]