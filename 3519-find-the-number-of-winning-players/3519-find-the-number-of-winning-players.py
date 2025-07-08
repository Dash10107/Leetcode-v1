class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        d = defaultdict(list)
        for x,y in pick:
            d[x].append(y)
        ans = 0
        for i in d:
            ch = max(Counter(d[i]).values())
            if ch>=i+1:
                ans+=1
        return ans