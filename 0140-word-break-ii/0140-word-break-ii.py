class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ws = set(wordDict)
        dp = defaultdict(list)
        def func(start):
            if start==len(s):
                return ['']
            if start in dp:
                return dp[start]
            res = []
            for end in range(start+1,len(s)+1):
                word = s[start:end]
                if word in ws:
                    subset = func(end)
                    for sent in subset:
                        res.append(word+ ('' if sent=='' else ' ')+ sent)
                    
            dp[start]=res
            return res
        return func(0)