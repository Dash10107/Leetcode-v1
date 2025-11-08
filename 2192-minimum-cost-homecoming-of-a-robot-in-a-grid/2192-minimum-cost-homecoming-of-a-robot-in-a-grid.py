class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        ans = 0

        if startPos[0] < homePos[0]:
            for i in range(startPos[0] + 1, homePos[0] + 1):
                ans += rowCosts[i]
        else:
            for i in range(startPos[0] - 1, homePos[0] - 1, -1):
                ans += rowCosts[i]


        if startPos[1] < homePos[1]:
            for j in range(startPos[1] + 1, homePos[1] + 1):
                ans += colCosts[j]
        else:
            for j in range(startPos[1] - 1, homePos[1] - 1, -1):
                ans += colCosts[j]

        return ans
