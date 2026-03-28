class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        par = list(range(n))
        size = [1]*n
        def find(x):
            if par[x]!=x:
                par[x]=find(par[x])
            return par[x]
        def union(a,b):
            pa,pb = find(a),find(b)
            if pa==pb:return
            if size[pa]<size[pb]:
                pa,pb=pb,pa
            par[pb]=pa
            size[pb]+=size[pa]
        for i in range(n):
            if lcp[i][i]!=n-i:return ''
            for j in range(n):
                if lcp[i][j]!=lcp[j][i]:return ''
        for i in range(n):
            for j in range(i+1,n):
                if lcp[i][j]>0:
                    union(i,j)
        rtochar = {};nxt=ord('a');ans=''
        for i in range(n):
            r = find(i)
            if r not in rtochar:
                if nxt>ord('z'):return ''
                rtochar[r]=chr(nxt)
                nxt+=1
            ans+=rtochar[r]
        temp = [[0]*n for i in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if ans[i]==ans[j]:
                    temp[i][j]=1
                    if i+1<n and j+1<n:
                        temp[i][j]+= temp[i+1][j+1]
                if temp[i][j]!=lcp[i][j]:return ''
        return ans