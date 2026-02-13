class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        a, b, c = 0, 0, 0
        visited = [{(0, 0): -1} for _ in range(7)]
        for i in range(len(s)):
            if s[i] == 'a':
                a += 1
            elif s[i] == 'b':
                b += 1
            else:
                c += 1
            keys = [(a - b, a - c),(c, a - b),(b, a - c),(a, b - c),]
            for j in range(4):
                if keys[j] in visited[j]:
                    ans = max(ans, i - visited[j][keys[j]])
                else:
                    visited[j][keys[j]] = i
            single= [(a, b),(a, c), (b, c)]
            for j in range(3):
                if single[j] in visited[j + 4]:
                    ans = max(ans, i - visited[j + 4][single[j]])
                else:
                    visited[j + 4][single[j]] = i
        return ans