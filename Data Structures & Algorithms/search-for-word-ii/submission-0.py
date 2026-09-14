class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        res = []
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                
                cur = cur.children[c]
            cur.word = word
        Rows = len(board)
        Cols = len(board[0])
        def dfs(r,c,node):
            if r < 0 or r >= Rows or c < 0 or c >= Cols:
                return
            
            char = board[r][c]
            if char == "#":
                return 
            
            if char not in node.children:
                return 
            
            node = node.children[char]
            if node.word is not None:
                res.append(node.word)
                node.word = None
            
            board[r][c] = '#'
            dfs(r+1,c,node)
            dfs(r,c+1,node)
            dfs(r-1,c,node)
            dfs(r,c-1,node)
            board[r][c] = char

        for r in range(Rows):
            for c in range(Cols):
                dfs(r,c,root)

        return res
            

