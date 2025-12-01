class Solution:
    def maxProfit(self, inventory: List[int], k: int) -> int:
        mod = 10**9+7
        h = [[-x, c] for x, c in Counter(inventory).items()]
        heapq.heapify(h)
        ans = 0
        while k:
            x, c = heapq.heappop(h)
            x = -x
            y = -h[0][0] if h else 0
            d = min(k // c, x - y)
            ans += c * d * (2*x - d + 1) // 2
            k -= d * c
            x -= d
            if k == 0 or x != y:
                ans += x * k
                break
            h[0][1] += c
        return ans % mod