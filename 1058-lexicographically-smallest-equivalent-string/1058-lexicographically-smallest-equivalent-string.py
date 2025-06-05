class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        parent = list(range(26))
        for a,b in zip(s1,s2):
            x,y = ord(a)-97,ord(b)-97
            rc,ry = find(x),find(y)
            if rc!=ry:
                if rc<ry:
                    parent[ry]=rc
                else:
                    parent[rc]=ry
        ans = []
        for i in baseStr:
            s = find(ord(i)-97)
            ans.append(chr(s+97))
        return ''.join(ans)