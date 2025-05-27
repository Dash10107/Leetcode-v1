class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        c = Counter(words)
        n = len(words[0])
        total = n*len(words)
        ans = []
        if len(s)< total:
            return []
        for i in range( len(s)-total+1 ):
            cd = {}
            j = i
            while j<i+total:
                word = s[j:j+n]
                cd[word] = cd.get(word, 0) + 1
                if word not in c:
                    break
                j+=n
            if cd==c:
                ans.append(i)
        return ans