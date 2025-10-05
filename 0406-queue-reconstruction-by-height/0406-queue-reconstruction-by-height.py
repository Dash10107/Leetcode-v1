class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0],x[1]))
        ans = []
        for peo in people:ans.insert(peo[1],peo)
        return ans