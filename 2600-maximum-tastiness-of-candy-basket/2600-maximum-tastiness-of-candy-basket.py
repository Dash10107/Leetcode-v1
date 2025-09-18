class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        def func(x):
            bask = [price[0]]
            for p in price[1:]:
                if p-bask[-1]>=x:
                    bask.append(p)
            return len(bask)>=k
        low = 0;high = price[-1]-price[0]
        ans = 0
        while low<=high:
            mid = (low+high)//2
            if func(mid):
                ans = mid
                low = mid+1
            else:
                high = mid-1
        return ans