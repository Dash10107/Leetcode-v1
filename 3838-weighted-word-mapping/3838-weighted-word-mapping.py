class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ''
        for word in words:
            weight = 0
            for ch in word:
                weight += weights[ord(ch)-ord('a')]
            mod = weight%26
            ans+=chr(ord('z')-mod)
        return ans