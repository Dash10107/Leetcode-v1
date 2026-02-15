class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        def solve(i, j, flag = True):
            while i >= 0 and j < n:
                if s[i] == s[j]:
                    i -= 1
                    j += 1
                elif flag:
                    mx = 0
                    if i > 0:
                        mx = max(mx, solve(i-1, j, False))
                    if j < n-1:
                        mx = max(mx, solve(i, j+1, False))
                    return max(mx, j - i - 1 + flag)
                else: break
            return j - i - 1 + flag
        
        mx = 1
        for i in range(n):
            mx = max(mx, solve(i, i))
            mx = max(mx, solve(i, i+1))
        
        return min(mx, n)