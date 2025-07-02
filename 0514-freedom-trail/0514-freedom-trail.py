class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n,m = len(ring),len(key)
        def dis(c,ne):
            bet = abs(c-ne)
            arr = n-bet
            return min(bet,arr)
        @cache
        def func(r,j):
            if j==m:
                return 0
            temp =float('inf') 
            for i in range(n):
                if ring[i]==key[j]:
                    steps = dis(r,i)+1 + func(i,j+1)
                    temp = min(steps,temp)
            return temp
        return func(0,0)