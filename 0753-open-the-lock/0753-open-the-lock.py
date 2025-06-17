class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def options(si):
            ans = []
            for i in range(4):
                cop = list(s)

                cop[i] = str((int(s[i]) - 1) % 10)
                ans.append(''.join(cop))
                cop = list(s)
                cop[i] = str((int(s[i]) + 1) % 10)
                ans.append(''.join(cop))
            return ans
        q = deque([('0000',0)])
        vis = set(deadends)
        vis.add('0000')
        while q:
            s,lev = q.popleft()
            if s == target:
                return lev
            if s in deadends:
                continue
            for opt in options(s):
                if opt not in vis:
                    q.append((opt,lev+1))
                    vis.add(opt)
 
        return -1