class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xcord = defaultdict(list)
        ycord = defaultdict(list)
        for x,y in buildings:
            xcord[x].append(y)
            ycord[y].append(x)
        for x in xcord:
            xcord[x].sort()
        for y in ycord:
            ycord[y].sort()
        ans = 0
        for x,y in buildings:
            row = xcord[x]
            col = ycord[y]
            pr = bisect_left(row,y)
            left = pr>0
            right = pr+1<len(row)

            pc = bisect_left(col,x)
            top = pc>0
            bottom = pc+1<len(col)
            if left and right and top and bottom:
                ans+=1
        return ans
