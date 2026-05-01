class Solution:
    def sortVowels(self, s: str) -> str:
        vows = {'a','e','i','o','u'}
        freq = Counter()
        for i,ch in enumerate(s):
            if ch in vows:
                freq[ch]+=1
        vowels=[]
        for i in range(len(freq)):
            val = freq.most_common(1)[-1][0]
            vowels+= [val]*freq[val]
            freq[val]=0
            
        ans = [];i=0
        for ch in s:
            if ch not in vows:ans.append(ch)
            else:
                ans.append(vowels[i])
                i+=1
        return ''.join(ans)