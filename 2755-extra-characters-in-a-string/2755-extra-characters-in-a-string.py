class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s);dic = set(dictionary)
        @lru_cache(None)
        def func(ind):
            if ind>=n:return 0
            curr = '';ans = n
            for i in range(ind,n):
                curr+= s[i]
                c = (0 if curr in dic else len(curr))+func(i+1)
                ans = min(c,ans)
            return ans
        return func(0)