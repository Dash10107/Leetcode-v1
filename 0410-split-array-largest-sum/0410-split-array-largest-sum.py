class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def func(x):
            curr=0;cnt=1
            for v in nums:
                if v+curr<=x:
                    curr+=v
                else:
                    curr=v
                    cnt+=1
                    if cnt>k:return False
            return True
        l,h = max(nums),sum(nums)
        while l<h:
            mid = (l+h)//2
            if func(mid):
                h = mid
            else:
                l=mid+1
        return l