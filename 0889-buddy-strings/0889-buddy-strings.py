class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        c,g = Counter(s),Counter(goal)
        if c!=g:
            return False
        s = sum(1 for c1,c2 in zip(s,goal) if c1!=c2)
        if s>2:
            return False
        if s==0 and max(c.values())==1:
            return False
        return True