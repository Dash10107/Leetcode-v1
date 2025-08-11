class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        a = [1 << i for i in range(n.bit_length()) if (n >> i) & 1]        
        mod = 10**9+7
        pref = [1] * (len(a) + 1)
        for i in range(1,len(a)+1):
            pref[i]= (a[i-1]*pref[i-1])%mod
        ans = []
        for l,r in queries:
            val = (pref[r+1] * pow(pref[l], mod-2, mod)) % mod
            ans.append(val)
        return ans