class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cows=0;bulls=0
        c1 = Counter(secret);c2 = Counter(guess)
        for ch in c1:
            if ch in c2:
                cows+= min(c1[ch],c2[ch])
        for i in range(len(guess)):
            if secret[i]==guess[i]:
                bulls+=1
        cows-= bulls
        return f'{bulls}A{cows}B'