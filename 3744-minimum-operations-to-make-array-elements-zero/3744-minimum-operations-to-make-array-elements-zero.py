class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def get(n):
            if n==0:return 0
            res,base,i=0,1,1
            while True:
                l = 1 <<(i-1)*2
                r = (1<<i * 2)-1
                if l>n:break
                count = min(r,n)-l+1
                res+= count*base
                base+=1
                i+=1
            return res
        ans = 0
        for l,r in queries:
            total = get(r)-get(l-1)
            ans+=(total+1)//2
        return ans