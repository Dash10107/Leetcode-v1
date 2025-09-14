class Solution:
    def spellchecker(self, words: List[str], queries: List[str]) -> List[str]:
        perf = set(words)
        caps ={};vows={}
        for word in words:
            wl = word.lower()
            if wl not in caps:caps[wl]=word
            wv = "".join('*' if c in 'aeiou' else c for c in wl)
            if wv not in vows:vows[wv]=word
        ans = []
        for word in queries:
            if word in perf:
                ans.append(word)
                continue
            wl = word.lower()
            if  wl in caps:
                ans.append(caps[wl])
                continue
            wv = "".join('*' if c in 'aeiou' else c for c in wl)
            if wv in vows:
                ans.append(vows[wv])
                continue
            ans.append('')
        return ans