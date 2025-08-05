class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        rem = 0
        n = len(baskets)
        vis = [False]*n
        for i in range(n):
            f = fruits[i]
            j = 0
            found = False
            while j<n :
                if  not vis[j] and baskets[j]>=f:
                    vis[j]=True
                    found = True
                    break
                else:j+=1
            
            if not found:
                rem+=1
        return rem