class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        n = len(citations)
        l,r = 0,len(citations)-1
        while l<=r:
            mid = (l+r)//2
            if citations[mid]>= n-mid:
                
                r = mid-1
            else:
                l= mid+1
        return n-l