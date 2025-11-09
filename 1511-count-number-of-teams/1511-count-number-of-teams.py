class Solution:
    def numTeams(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        for i in range(n):
            ll,lg,rl,rg=0,0,0,0
            for j in range(i):
                if arr[j]<arr[i]:
                    ll+=1
                elif arr[j]>arr[i]:
                    lg+=1
            for k in range(i+1,n):
                if arr[i]<arr[k]:
                    rg+=1
                elif arr[i]>arr[k]:
                    rl+=1
            ans+= ll*rg + rl*lg
        return ans