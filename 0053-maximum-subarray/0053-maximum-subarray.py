class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        def cross(l,mid,h):
            left = float('-inf')
            s = 0
            for i in range(mid,l-1,-1):
                s+=arr[i]
                left = max(left,s)
            s = 0
            right = float('-inf')
            for j in range(mid,h+1):
                s+=arr[j]
                right = max(right,s)
            return max([left,right,left+right-arr[mid]])

        def find(l,h):
            if l>h:
                return float('-inf')
            elif l==h:
                return arr[h]
            else:
                mid = (l+h)//2
                return max([find(l,mid),find(mid+1,h),cross(l,mid,h)])
        return find(0,len(arr)-1)