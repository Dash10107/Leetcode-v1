class Solution:
    def trap(self, arr: List[int]) -> int:
        ans = 0
        pm,sm = 0,0 
        l,r = 0,len(arr)-1
        while l<r:
            if arr[l]<=arr[r]:
                if pm>arr[l]:
                    ans+= pm-arr[l]
                else:
                    pm = arr[l]
                l+=1
            else:
                if sm>arr[r]:
                    ans+= sm-arr[r]
                else:
                    sm = arr[r]
                r-=1
        return ans