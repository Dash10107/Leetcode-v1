class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mis,mas=[],[]
        ans = 0
        for arr in arrays:
            mi = min(arr);ma= max(arr)
            if mis:
                ans = max(ans,ma- mis[0])
            if mas:
                ans = max(ans,-mas[0]- mi)
            heappush(mis,mi)
            heappush(mas,-ma)
        return ans