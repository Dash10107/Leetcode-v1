class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(k):
            c = defaultdict(int)
            l,ans = 0,0
            for r,x in enumerate(nums):
                c[x]+=1
                while len(c)>k:
                    c[nums[l]]-=1
                    if c[nums[l]]==0:del c[nums[l]]
                    l+=1
                ans+= r-l+1
            return ans
        return atmost(k)-atmost(k-1)