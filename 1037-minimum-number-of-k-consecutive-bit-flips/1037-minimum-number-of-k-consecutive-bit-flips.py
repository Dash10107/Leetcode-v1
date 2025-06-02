class Solution:
    def minKBitFlips(self, arr: List[int], k: int) -> int:
        ans = 0
        flipped = [0]*len(arr)
        flip =0
        for i in range(len(arr)):
            if i>=k:
                flip ^= flipped[i-k]
            if arr[i]==flip:
                if i+k>len(arr):
                    return -1
                flipped[i]=1
                flip^=1
                ans+=1
        return ans