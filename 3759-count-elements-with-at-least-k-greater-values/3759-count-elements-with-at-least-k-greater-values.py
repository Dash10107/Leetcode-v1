class Solution:
    def countElements(self, arr: List[int], k: int) -> int:
        arr.sort()
        i=0;n=len(arr);ans=0
        while i<n:
            a = arr[i]
            j=i+1
            while j<n and arr[j]==a:j+=1
            if n-j>=k:ans+=(j-i)
            i=j
        return ans