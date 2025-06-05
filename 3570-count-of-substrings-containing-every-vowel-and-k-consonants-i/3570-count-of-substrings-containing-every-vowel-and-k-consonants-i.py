class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        c = Counter('aeiou')
        ans= 0
        for i in range(len(word)-4-k):
            vow,con = set(),[]
            while i<len(word):
                if word[i] in c:
                    vow.add(word[i])
                else:
                    con.append(word[i])
                if len(vow)==5 and len(con)==k:
                    ans+=1
                if len(con)>k:
                    break
                i+=1
        return ans