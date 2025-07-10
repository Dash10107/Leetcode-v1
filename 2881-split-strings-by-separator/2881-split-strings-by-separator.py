class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            for ch in word.split(separator):
                if ch!="":
                    ans.append(ch)
        return ans