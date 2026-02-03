class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        p = 0
        while p+1<n and nums[p]<nums[p+1] :
            p+=1
        if p==0 or p==n-1:
            return False
        q = p
        while q+1<n and nums[q+1]<nums[q]:
            q+=1
        if q==p or q==n-1:
            return False
        last = q
        while last+1<n and nums[last]<nums[last+1]:
            last+=1
        if last==q:
            return False
        return last==n-1