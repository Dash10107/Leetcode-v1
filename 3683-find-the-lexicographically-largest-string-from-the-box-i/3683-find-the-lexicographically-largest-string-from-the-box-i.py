class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        ans=''
        m = len(word)-numFriends+1
        if numFriends==1:
            return word
        for i in range(len(word)):
            ans = max(ans,word[i:i+m])

        return ans