class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word = list(word)
        for i in range(len(word)):
            if not word[i].isdigit():
                word[i]=' '
        words= ''.join(word).split(' ')
        s = set()
        for ch in words:
            if ch!='':s.add(int(ch))
        return len(s)
