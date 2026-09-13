class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

        

    def search(self, word: str) -> bool:
        def dfs(i,node):
            for j in range(i,len(word)):
                c = word[j]
                if c == ".":
                    for child in node.children.values():
                        if dfs(j + 1,child):
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            return node.endOfWord
        return dfs(0,self.root) 

            
