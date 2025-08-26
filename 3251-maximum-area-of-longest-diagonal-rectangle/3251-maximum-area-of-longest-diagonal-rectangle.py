class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = 0
        dia=0
        for l,w in dimensions:
            diag = sqrt(l**2 + w**2)
            if diag>dia:
                dia = diag
                ans = l*w
            elif diag==dia:
                ans = max(ans,l*w)
        return ans