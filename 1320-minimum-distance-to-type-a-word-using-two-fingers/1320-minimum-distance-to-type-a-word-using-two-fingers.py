class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(pre,curr):
            if pre==None:return 0
            x1,y1 = divmod(ord(pre)-ord('A'),6)
            x2,y2 = divmod(ord(curr)-ord('A'),6)
            return abs(x1-x2)+abs(y1-y2)
        @cache
        def func(i,l,r):
            if i==len(word):return 0
            n1 = dist(l,word[i]) + func(i+1,word[i],r)
            n2 = dist(r,word[i]) +func(i+1,l,word[i])
            return min(n1,n2)
        return func(0,None,None)
