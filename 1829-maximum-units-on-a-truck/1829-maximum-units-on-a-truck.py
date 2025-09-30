class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], s: int) -> int:
        boxTypes.sort(key=lambda x:-x[1])
        ans =0
        for b,u in boxTypes:
            if s-b>=0:
                s-=b
                ans+=(u*b)
            elif s and b>=s:
                ans+=(u*s)
                s=0
            else:
                break
        return ans