class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:
        n = len(stones)
        @lru_cache(None)
        def func(i):
            if i>=n:return 0
            one = stones[i]-func(i+1);two=float('-inf')
            if i+1<n:
                two = stones[i]+stones[i+1]-func(i+2)
            three = float('-inf')
            if i+2<n:
                three = stones[i]+stones[i+1]+stones[i+2]-func(i+3)
            return max(one,two,three)
        ans = func(0)
        if ans>0:return "Alice"
        elif ans<0:return "Bob"
        else: return "Tie"