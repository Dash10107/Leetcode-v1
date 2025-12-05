class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = max(nums)+1
        par = list(range(n));size=[1]*n
        def find(x):
            while par[x]!=x:
                par[x]=par[par[x]]
                x = par[x]
            return x
        def union(a,b):
            pa,pb = find(a),find(b)
            if pa!=pb:
                if size[pa]<size[pb]:
                    pa,pb=pb,pa
                par[pb]=pa
                size[pa]+=size[pb]

        seen={}
        for x in nums:
            temp=x;f=2
            while f*f<=temp:
                if temp%f==0:
                    if f not in seen:
                        seen[f]=x
                    else:union(x,seen[f])
                    while temp%f==0:
                        temp//=f
                f+=1
            if temp>1:
                if temp not in seen:seen[temp]=x
                else:union(x,seen[temp])
        cnt = {};ans=0
        for x in nums:
            pa = find(x)
            cnt[pa]=cnt.get(pa,0)+1
            ans = max(ans,cnt[pa])
        return ans