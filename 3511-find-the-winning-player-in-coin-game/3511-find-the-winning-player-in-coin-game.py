class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        alice = False
        while x>=1 and y>=4:
            x-=1
            y-=4
            alice = not alice
        return  "Alice" if alice else "Bob"