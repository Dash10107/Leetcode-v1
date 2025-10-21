class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hoftd = [0]*24
        total = 0
        for h in hours:
            total+=hoftd[h%24]
            r = (24-h%24)%24
            hoftd[r]+=1
        return total