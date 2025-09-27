class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        c = Counter(s)
        d = defaultdict(str)
        for ch in c:
            d[c[ch]]+=ch
        key = 0;l = 0
        for val in d:
            if len(d[val])>l:
                l = len(d[val])
                key = val
            elif len(d[val])==l:
                l = len(d[val])
                key = max(val,key)
        return d[key]