class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        s = Counter(str(n))
        key = float('inf')
        val = float('inf')
        for ch in s:
            if s[ch]<val:
                key = int(ch)
                val = s[ch]
            elif s[ch]==val:
                key = min(int(ch),int(key))
        return int(key)