class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = defaultdict(int)
        ans = 0;n = len(fruits)
        l,r = 0,0
        while r<n:
            t = fruits[r]
            dic[t]+=1
            if len(dic)>2:
                dic[fruits[l]]-=1
                if dic[fruits[l]]==0:del dic[fruits[l]]
                l+=1
            if len(dic)<=2:
                ans  = max(ans,r-l+1)
            r+=1
        return ans