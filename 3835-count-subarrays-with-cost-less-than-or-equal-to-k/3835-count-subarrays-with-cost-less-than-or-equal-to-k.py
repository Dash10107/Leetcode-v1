class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = deque();mn = deque()
        j = 0;n=len(nums)
        ans = 0
        for i in range(n):
            while mx and nums[mx[-1]]<=nums[i]:
                mx.pop()
            mx.append(i)
            while mn and nums[mn[-1]]>=nums[i]:
                mn.pop()
            mn.append(i)
            while j<=i:
                l=i-j+1
                cmx = nums[mx[0]]
                cmn = nums[mn[0]]
                if (cmx-cmn)*l<=k:
                    break
                if mx[0]==j:
                    mx.popleft()
                if mn[0]==j:
                    mn.popleft()
                j+=1
            ans+=(i-j+1)
        return ans