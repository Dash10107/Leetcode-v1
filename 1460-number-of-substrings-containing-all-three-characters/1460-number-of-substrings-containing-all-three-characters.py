class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        arr = [-1,-1,-1]
        ans=0
        for i,ch in enumerate(s):
            arr[ord(ch)-ord('a')]=i
            ans+= (1+min(arr))
        return ans