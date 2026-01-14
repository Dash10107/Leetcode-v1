class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        pos = [[] for _ in range(26)]
        for i,ch in enumerate(s):
            pos[ord(ch)-ord('A')].append(i)
        ans = 0 
        for arr in pos:
            for i in range(len(arr)):
                prev = arr[i-1] if i>0 else -1
                nextt = arr[i+1] if i+1<len(arr) else n
                left = arr[i]-prev
                right = nextt-arr[i]
                ans+= left*right
        return ans