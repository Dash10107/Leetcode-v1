class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        l,r = 1,n-1
        while l<r:
            mid = (l+r)//2
            c = 0
            for ni in nums:
                if ni<=mid:
                    c+=1
            if c>mid:
                r = mid
            else:
                l = mid+1
        return l