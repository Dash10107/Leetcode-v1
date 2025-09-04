class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s)<k:return 0
        freq = Counter(s)
        for ch in freq:
            if freq[ch]<k:
                parts = s.split(ch)
                return max(self.longestSubstring(p,k) for p in parts)
        return len(s)