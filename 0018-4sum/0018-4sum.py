class Solution:
    def fourSum(self, arr: List[int], target: int) -> List[List[int]]:
        arr.sort()
        ans = set()
        n = len(arr)
        if n<=3:
            return []
        for i in range(n-3):
            for j in range(i+1,n-2):
                half = arr[i]+arr[j]
                k = j+1
                l = n-1
                while k<l:
                    temp = arr[k]+arr[l]
                    if temp+half == target:
                        ans.add((arr[i],arr[j],arr[k],arr[l]))
                        k+=1
                    elif temp+half>target:
                        l-=1
                    else:
                        k+=1
        return list(ans)