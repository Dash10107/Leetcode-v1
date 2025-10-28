class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        ans=0;pref=0;suff=sum(nums)
        for n in nums:
            pref+=n
            suff-=n
            if n!=0:continue
            if pref==suff:ans+=2
            if abs(pref-suff)==1:ans+=1
        return ans