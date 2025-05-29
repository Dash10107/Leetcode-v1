class Solution:
    def canAliceWin(self, n: int) -> bool:
        i = 10
        turn = True
        if n<i:
            return False
        while n-i>=0:
            n-=i
            i-=1
            turn = not turn
            print(n,turn)
        return not turn
