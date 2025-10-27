class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def can(k):
            curr  = position[0];i=1;cnt=1
            while i<len(position):
                if position[i]-curr>=k:
                    curr=position[i]
                    i+=1
                    cnt+=1
                else:
                    i+=1
            return cnt>=m
                    
        left = 1;right=position[-1]-position[0]
        ans = 0
        while left<=right:
            mid = (left+right)//2
            if can(mid):
                ans = mid
                left = mid+1
            else:
                right = mid-1
        return ans