class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        bs = int(ceil(sqrt(n)))
        buks = [[] for _ in range(bs)]
        for i,b in enumerate(baskets):
            bi = i//bs
            buks[bi].append((b,i))
        for b in buks:
            b.sort()
        ans = 0
        for cnt in fruits:
            for b in buks:
                if b and b[-1][0]>=cnt:
                    chose = min((i,bb) for bb,i in b if bb>=cnt)
                    b.remove((chose[1],chose[0]))
                    break
            else:
                ans+=1
        return ans