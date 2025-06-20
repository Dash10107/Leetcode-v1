class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        def func(good):
            score,bad=0,0
            ans =0 
            for ch in s:
                if ch in good:
                    score+=1
                else:
                    score-=1
                    bad+=1
                ans = max(ans,score+ 2*min(k,bad))
            return ans
        res = 0
        for dic in ['NE','NW','SE','SW']:
            res = max(res,func(dic))
        return res