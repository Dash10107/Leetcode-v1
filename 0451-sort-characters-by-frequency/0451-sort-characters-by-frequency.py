class Solution:
    def frequencySort(self, s: str) -> str:
        cc=Counter(s).most_common()
        ans = ''
        for ch,val in cc:
            ans += ch*val
        return ans