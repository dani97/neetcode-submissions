class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordGraph = defaultdict(list)
        wordList.append(beginWord)
        wordList = set(wordList)

        def findConnection(word):
            edges = []
            for other in wordList:
                if word == other: continue
                cf = True

                for i in range(len(word)):
                    if word[i] != other[i]:
                        if cf:
                            cf = False
                        else:
                            break
                else:
                    edges.append(other)
            return edges

        for word in wordList:
            wordGraph[word] = findConnection(word)
        wordGraph[beginWord] = findConnection(beginWord)
        
        print(wordGraph)

        visited = set()
        queue = deque()
        depth = 0
        queue.append(beginWord)

        while len(queue) > 0:
            depth += 1
            currentWords = len(queue)
            for key in range(currentWords):
                word = queue.popleft()
                if word == endWord:
                    return depth
                if word not in visited:
                    visited.add(word)
                    for nxt in wordGraph[word]:
                        queue.append(nxt)
        return 0