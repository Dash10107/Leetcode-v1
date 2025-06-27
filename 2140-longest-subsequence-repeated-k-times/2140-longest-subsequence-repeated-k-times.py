class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        c = Counter(s)

        chars = options = {char for char, v in c.items() if v >= k}
        if not options:
            return ''
        def check(sub):
            sub_it = iter(sub*k)
            it = iter(s)
            return all(ch in it for ch in sub_it)
        for i in range(len(s)//k-1):
            new = set()
            for op in options:
                for ch in chars:
                    if op[1:]+ch in options and check(op+ch):
                        new.add(op+ch)
            if not new:
                return max(options)
            options = new
        return max(options)