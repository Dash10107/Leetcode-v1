class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        heap = []
        for i in c:
            heapq.heappush(heap,(-c[i],i))
        ans = []
        while k>0:
            _,word = heapq.heappop(heap)
            ans.append(word)
            k-=1
        return ans
