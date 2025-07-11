class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for det in details:
            age = det[11:13]
            if int(age)>60:
                ans+=1
        return ans