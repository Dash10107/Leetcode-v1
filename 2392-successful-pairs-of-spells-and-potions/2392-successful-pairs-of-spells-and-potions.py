class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        ans = []
        for s in spells:
            if s==0:
                ans.append(0)
                continue
            thres = (success+s-1)//s
            ind = bisect_left(potions,thres)
            ans.append(n-ind)
        return ans