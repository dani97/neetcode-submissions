class WordDictionary:

    def __init__(self):
        # Key = alphabet
        # value = hmap < alphabet, hmap<>>
        self.root = dict()

    def addWord(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node:
                node[i] = {}
            node = node[i]
        node["$"] = word
    
    def search(self, node: dict, ch: str):
        if "$" in node:
            return (node["$"], True)
        if ch in node:
            return (node[ch], True)
        else:
            return ({}, False)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        word_dict = WordDictionary()
        for word in words:
            word_dict.addWord(word)
        
        m = len(board)
        n = len(board[0])
        result = set()
        hs = set()

        def dfs(i, j, node):
            if "$" in node:
                result.add(node["$"])
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if (i,j) in hs:
                return False
            if board[i][j] not in node:
                return False
            
            hs.add((i,j))
            left = dfs(i-1, j , node[board[i][j]])
            right = dfs(i+1, j , node[board[i][j]])
            up = dfs(i, j-1 , node[board[i][j]])
            down = dfs(i, j+1 , node[board[i][j]])
            hs.remove((i,j))
            return left or right or up or down


        for i in range(m):
            for j in range(n):
                (cmap, proceed) = word_dict.search(word_dict.root, board[i][j])
                if proceed:
                    dfs(i, j, word_dict.root)
        return list(result)
