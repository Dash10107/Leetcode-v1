class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        l,r = 0,len(arr)-1
        while l<=r:
            mid = arr[l]+arr[r]
            if mid==target:
                return [l+1,r+1]
            elif target<mid:
                r-=1
            else:
                l+=1
        