class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        pre = [-1]*(n+1)
        for i in range(n):
            if i==0 or  s[i-1]=='0':pre[i+1]=i
            else:pre[i+1]=pre[i]
        ans =0
        for i in range(1,n+1):
            j = i
            c= 1 if s[i-1]=='0' else 0
            while j>0 and c*c <= n:
                cnt1 = (i-pre[j])-c
                if cnt1>= c*c:
                    ans+=min(j-pre[j],cnt1 -c * c + 1)
                j = pre[j]
                c+=1
        return ans