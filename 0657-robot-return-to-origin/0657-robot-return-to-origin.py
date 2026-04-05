class Solution:
    def judgeCircle(self, moves: str) -> bool:
        rob = [0,0]
        for m in moves:
            if m=='U':rob[1]+=1
            elif m=='D':rob[1]-=1
            elif m=='L':rob[0]+=1
            elif m=='R':rob[0]-=1
        return rob==[0,0]