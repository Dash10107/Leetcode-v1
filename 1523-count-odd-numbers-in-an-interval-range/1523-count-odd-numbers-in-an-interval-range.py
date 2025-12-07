class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = (high-low+1)//2
        if low&1 and high&1:
            ans+=1
        return ans
        
