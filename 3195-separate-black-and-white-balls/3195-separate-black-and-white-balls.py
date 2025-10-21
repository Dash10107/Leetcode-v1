class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        bc = 0
        for ch in s:
            if ch == '1':
                bc+=1
            else:
                ans+=bc
        return ans