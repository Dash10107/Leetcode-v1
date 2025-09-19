class Solution:
    def maxSatisfaction(self, sat: List[int]) -> int:
        sat.sort(reverse=True)
        s=0;ans=0
        for i in sat:
            if s+i>0:
                ans+= i+s
                s+=i
        return ans
        