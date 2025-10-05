class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        dirr = [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]
        qs = set()
        for rq,cq in queens:qs.add((rq,cq))
        n=8;m=8
        ans = set()
        q = deque()
        for dr, dc in dirr:
            q.append((king[0] + dr, king[1] + dc, dr, dc))
        while q:
            i,j,dr,dc = q.popleft()
            if i<0 or j<0 or i>=n or j>=m :
                continue
            if (i,j) in qs:
                ans.add((i,j))
                continue
            q.append((i+dr,j+dc,dr,dc))
        return list(ans)