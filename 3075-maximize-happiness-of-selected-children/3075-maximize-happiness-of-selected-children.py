class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        ans=0;i=0;n=len(happiness)-1
        while i<k:
            ans+= max(0,happiness[n-i]-i)
            i+=1
        return ans