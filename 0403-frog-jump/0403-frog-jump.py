class Solution:
    def canCross(self, stones: List[int]) -> bool:
        s = set(stones)
        vis = set()
        def func(val,last):
            if (val+last not in s) or ((val,last) in vis):
                return False
            if val+last== stones[-1]:
                return True
            vis.add((val,last))
            return func(val+last,last) or func(val+last,last-1) or func(val+last,last+1)
        return func(stones[0],1)