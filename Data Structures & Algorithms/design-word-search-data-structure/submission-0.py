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
        node["$"] = {}
                
    def search(self, word: str) -> bool:
        def search_for_node(node, word) -> bool:
            for i, ch in enumerate(word):
                if ch not in node:
                    if ch == ".":
                        for x in node:
                            if x != "$" and search_for_node(node[x], word[i+1:]):
                                return True
                    return False
                else:
                    node = node[ch]
            return "$" in node

        return search_for_node(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)