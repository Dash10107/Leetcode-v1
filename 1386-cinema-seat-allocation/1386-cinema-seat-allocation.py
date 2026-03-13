class Solution:
    def maxNumberOfFamilies(self, n: int, reserved: List[List[int]]) -> int:
        # mat = [[False]*10 for _ in range(n)]
        rows = defaultdict(set)
        for r,c in reserved:
            rows[r].add(c)
        ans = (n-len(rows))*2
        for r in rows:
            s = rows[r]
            left = not (2 in s or 3 in s or 4 in s or 5 in s)
            right = not (6 in s or 7 in s or 8 in s or 9 in s)
            mid = not (7 in s or 4 in s or 5 in s or 6 in s)
            if left and right:ans+=2
            elif left or mid or right:ans+=1
        return ans