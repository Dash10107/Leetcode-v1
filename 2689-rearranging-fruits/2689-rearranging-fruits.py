class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        c1 = Counter(basket1); c1.subtract(Counter(basket2))
        toSwap = []
        for key,val in c1.items():
            if val%2!=0:
                return -1
            toSwap += [key]* (abs(val)//2)
        toSwap.sort()
        ans = 0
        m = min(basket1+basket2)
        for i in range(len(toSwap)//2):
            ans+= min(2*m,toSwap[i])
        return ans