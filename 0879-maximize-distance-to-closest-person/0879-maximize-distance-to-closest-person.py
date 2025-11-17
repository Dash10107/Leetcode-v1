class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        i=0;ans=1
        n=len(seats);curr=0;first=True
        for s in seats:
            if s==0:
                curr+=1
            else:
                if first:
                    ans = max(ans,curr)
                    first=False
                else:
                    ans = max(ans,(curr+1)//2)
                curr=0
        if seats[-1]!=1:
            ans = max(ans,curr)
        return ans