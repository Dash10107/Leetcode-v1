class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        suff = [0]*(n+1)
        for i in range(n-1,-1,-1):
            suff[i]= (1 if customers[i]=='Y' else 0 )+suff[i+1]
        ans = float('inf');res = 0;pref=0
        for i in range(n+1):
            if pref+suff[i]<ans:
                ans = pref+suff[i]
                res = i
            pref+=(1 if i<n and customers[i]=='N' else 0)
        return res