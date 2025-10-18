class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        ans =len(c)
        for key,val in sorted(c.items(),key=lambda x:x[1]):
            if val<=k:
                ans-=1
                k-=val
            else:break
        return ans