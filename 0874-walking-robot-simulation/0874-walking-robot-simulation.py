class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(tuple(ob) for ob in obstacles)
        ans =0
        dirr= [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x,y =0,0;curr=0
        for c in commands:
            if c==-1:
                curr = (curr+1)%4
                continue
            if c==-2:
                curr=(curr+3)%4
                continue
            dx,dy = dirr[curr]
            for _ in range(c):
                nx,ny = x+dx,y+dy
                if (nx,ny) in obstacles:break
                x,y = nx,ny
            ans = max(ans,x*x+y*y)
        return ans