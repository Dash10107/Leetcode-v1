class Solution:
    def decodeCiphertext(self, enc: str, rows: int) -> str:
        n = len(enc)
        cols = n // rows
        mat = [[' '] * cols for _ in range(rows)]
        i = j = ch = 0
        while ch < n:
            mat[i][j] = enc[ch]
            ch += 1
            j += 1
            if j == cols:
                j = 0
                i += 1

        res = []
        for k in range(cols):
            i, j = 0, k
            while i < rows and j < cols:
                res.append(mat[i][j])
                i += 1
                j += 1
        return ''.join(res).rstrip()