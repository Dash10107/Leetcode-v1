class Solution:
    def findPeaks(self, mounts: List[int]) -> List[int]:
        ans = [];n=len(mounts)
        for i in range(1,n-1):
            if mounts[i]>mounts[i-1] and mounts[i]>mounts[i+1]:
                ans.append(i)
        return ans