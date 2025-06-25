class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        s = SortedSet(list(range(n)))
        for u,v in queries:
            t = s.bisect_right(u)
            while s[t]<v:
                s.pop(t)
            res.append(len(s)-1)
        return res