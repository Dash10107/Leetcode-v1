class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(' ')
        ans = []
        for word in arr:
            ans.append(word[::-1]+' ')
        return  ''.join(ans)[:-1]