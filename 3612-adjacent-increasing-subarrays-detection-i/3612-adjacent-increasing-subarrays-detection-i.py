class Solution:
    def hasIncreasingSubarrays(self, arr: List[int], k: int) -> bool:
        def check(ar):
            for i in range(1,len(ar)):
                if ar[i]<=ar[i-1]:
                    return False
            return True
        for i in range(len(arr)-(2*k)+1):
            if check(arr[i:i+k]) and check(arr[i+k:i+k+k]):
                return True
        return False