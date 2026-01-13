class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        n = len(squares)
        area = 0
        l,h = 0,0
        for s in squares:
            yi,li = s[1],s[2]
            a = li * li
            area +=a
            h = max(h,yi+li)
        targ = area/2.0
        tol = 1e-6
        while h-l>tol:
            mid = (l+h)/2.0
            bel = 0
            for s in squares:
                yi,li = s[1],s[2]
                top = yi + li
                if mid <=yi:
                    continue
                elif mid >=top:
                    bel += li*li
                else:
                    bel += li * (mid-yi)
            if bel < targ:
                l = mid
            else:
                h = mid
        return h