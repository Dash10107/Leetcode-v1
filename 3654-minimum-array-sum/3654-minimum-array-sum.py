class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)
        @lru_cache(None)
        def func(i,o1,o2):
            if i==n:return 0
            s = nums[i] + func(i+1,o1,o2)
            if o1>0 and o2>0:
                m1 = (nums[i]+1)//2
                m2 = (m1-k if m1>=k else m1)
                s = min(s, m2 + func(i+1,o1-1,o2-1))
                mm2 = (nums[i]-k if nums[i]>=k else nums[i])
                mm1 = (mm2+1)//2
                s = min(s, mm1 + func(i+1,o1-1,o2-1))
            if o1>0: 
                m1 = (nums[i]+1)//2
                s = min(s,m1 + func(i+1,o1-1,o2))
            if o2>0:
                m2 = (nums[i]-k if nums[i]>=k else nums[i])
                s =min (s,m2 + func(i+1,o1,o2-1))
            return s
        return func(0,op1,op2)
    