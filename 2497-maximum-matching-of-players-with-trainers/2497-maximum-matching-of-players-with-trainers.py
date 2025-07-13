class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()
        i=0;j=0;ans=0
        m = len(trainers);n=len(players)
        while i<n:
            p = players[i]
            while j<m and trainers[j]<p:
                j+=1
            if j==m:
                break
            elif p<=trainers[j]:
                ans+=1
                j+=1
            i+=1
        return ans