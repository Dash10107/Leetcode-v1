class Solution:
    def canBeTypedWords(self, text: str, broks: str) -> int:
        arr = text.split(' ')
        ans = 0
        st =set(broks)
        for word in arr:
            if all(ch not in st for ch in word):
                ans+=1
        return ans