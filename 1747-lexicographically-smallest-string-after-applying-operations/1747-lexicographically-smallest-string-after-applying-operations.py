class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        s = tuple(s)
        def rot(arr):
            return arr[-b:]+arr[:-b]
        def add(arr):
            new = ['']*len(arr)
            for i in range(len(arr)):
                if i%2==1:new[i]= str((int(arr[i])+a)%10)
                else:new[i]=arr[i]
            return tuple(new)
        vis = set()
        def func(ss):
            if ss in vis:return ss
            vis.add(ss)
            ad = add(ss);ro=rot(ss)
            return min(ad,ro,func(ad),func(ro))
        return ''.join(func(s))