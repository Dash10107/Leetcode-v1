class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0,1)])
        ans = 0
        while q:
            n = len(q)
            for _ in range(n):
                pos,speed = q.popleft()
                if pos==target:
                    return ans
                q.append((pos+speed,speed*2))
                rev = -1 if speed>0 else 1
                if (pos+speed<target and speed<0) or ( pos+speed>target and speed>0):
                    q.append((pos,rev))
            ans+=1