class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k!=0:return False
        c = Counter(nums)
        for i in sorted(c):
            f = c[i]
            if f>0:
                for j in range(i,i+k):
                    if c[j]<f:
                        return False
                    c[j]-=f
        return True