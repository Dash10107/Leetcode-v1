class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        plate =-1
        suff = [-1]*(n)
        for i in range(n-1,-1,-1):
            plate= i if s[i]=='|' else plate
            suff[i]= plate
        pref = [-1]*n
        plate = -1
        for i in range(n):
            plate= i if s[i]=='|' else plate
            pref[i]=plate 
        ans = []
        pss = [0]*(n+1)
        for i in range(n):
            pss[i+1]= pss[i]+(1 if s[i]=='*' else 0)
        for l,r in queries:
            left = suff[l]
            right = pref[r]
            if left==-1 or right==-1 or left>=right:
                ans.append(0)
            else:
                ans.append(pss[right]-pss[left])
        return ans