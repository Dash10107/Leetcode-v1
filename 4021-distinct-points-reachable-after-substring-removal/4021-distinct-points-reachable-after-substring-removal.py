class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        n = len(s)
        move = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
        pref = [(0,0)]*(n+1)
        for i in range(n):
            dx,dy = move[s[i]]
            px,py = pref[i]
            pref[i+1]= (px+dx,dy+py)
        tot = pref[n]
        seen = set()
        for i in range(n-k+1):
            sx = pref[i+k][0]-pref[i][0]
            sy = pref[i+k][1]-pref[i][1]
            fin = (tot[0]-sx,tot[1]-sy)
            seen.add(fin)
        return len(seen)