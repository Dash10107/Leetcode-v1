class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0;n=len(colors);i=0
        while i<n:
            j = i
            temp = 0;tot=0
            while j<n and colors[j]==colors[i]:
                temp = max(temp,neededTime[j])
                tot+=neededTime[j]
                j+=1
            ans+= (tot-temp)
            i=j
        return ans