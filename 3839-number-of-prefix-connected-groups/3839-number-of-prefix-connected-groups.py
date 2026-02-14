class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        dic = defaultdict(int)
        for word in words:
            if len(word)<k:continue
            dic[word[:k]]+=1
        ans = 0
        for key,val in dic.items():
            if val>1:ans+=1
        return ans