class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores complete word at leaf for easy retrieval

def buildTrie(words):
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word
    return root
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = buildTrie(words)
        ans = set()
        n,m = len(board),len(board[0])
        def dfs(i,j,node):
            nonlocal ans
            char = board[i][j]
            if char not in node.children:return
            node = node.children[char]
            if node.word:ans.add(node.word)
            board[i][j]='-'
            for nr,nc in [(0,1),(1,0),(-1,0),(0,-1)]:
                ni,nj =i+nr,j+nc
                if 0<=ni<n and 0<=nj<m and board[ni][nj]!='-':
                    dfs(ni,nj,node)
            board[i][j]=char
        for i in range(n):
            for j in range(m):
                dfs(i,j,root)
        return list(ans)