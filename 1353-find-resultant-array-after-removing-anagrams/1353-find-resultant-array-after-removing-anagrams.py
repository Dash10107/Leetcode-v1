class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        prev = Counter(words[0])
        ans = set()
        for i in range(1,len(words)):
            c = Counter(words[i])
            if prev==c:
                ans.add(i)
            else:
                prev = c
        arr =  []
        for i in range(len(words)):
            if i not in ans:
                arr.append(words[i])
        return arr