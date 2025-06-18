class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        temp = []
        for i in range(len(nums)):
            if len(temp)==3:
                ans.append(temp)
                temp = []
            if temp and nums[i]-temp[-1]<=k and nums[i]-temp[0]<=k:
                temp.append(nums[i])
            elif not temp:
                temp.append(nums[i])
            else:
                return []
        ans+= [temp]
        return ans

            