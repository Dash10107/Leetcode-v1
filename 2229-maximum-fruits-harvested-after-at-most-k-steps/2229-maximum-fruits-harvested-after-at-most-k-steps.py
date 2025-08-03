class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        poss = [pos for pos,_ in fruits]
        pref = [0]*(n+1)
        for i in range(n):
            pref[i+ 1] = pref[i]+fruits[i][1]
        m = 0
        left = 0
        for right in range(n):
            posl = poss[left]
            posr = poss[right]
            cost = (posr-posl) + min(abs(startPos-posl),abs(startPos-posr))
            while left<=right and cost>k:
                left+=1
                if left>right:
                    break
                posl = poss[left]
                cost = (posr-posl) + min(abs(startPos-posl),abs(startPos-posr))
            if left<=right:
                curr = pref[right+1]-pref[left]
                m = max(m,curr)
        return m
