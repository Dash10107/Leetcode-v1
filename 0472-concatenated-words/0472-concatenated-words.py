class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        @cache
        def dfs(stri):
            val=False
            for i in range(1,len(stri)):
                left = stri[:i]
                right = stri[i:]
                if left in words:
                    if right in words or  dfs(right):
                        val=True
                        break
            return val
        ans=[]
        for word in words:
            if dfs(word):ans.append(word)
        return ans