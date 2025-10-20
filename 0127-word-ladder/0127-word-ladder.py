class Solution:
    def ladderLength(self, begin: str, end: str, words: List[str]) -> int:
        words = set(words)
        q  = deque([begin])
        ans=1;vis=set();vis.add(begin)
        while q:
            s = len(q)
            for i in range(s):
                node = q.popleft()
                if node==end:return ans
                for j in range(len(node)):
                    temp = node
                    for c in range(ord('a'),ord('z')+1):
                        temp=temp[:j]+chr(c)+temp[j+1:]

                        if temp in words and temp not  in vis:
                            q.append(temp)
                            vis.add(temp)
            ans+=1
        return 0