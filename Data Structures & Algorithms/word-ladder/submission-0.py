from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        l = len(beginWord)
        tree = defaultdict(list)
        for word in wordList:
            for i in range(l):
                pattern = word[:i] + "*" + word[i+1:]
                tree[pattern].append(word)

        answers = set()
        for i in range(l):
            answers.add(endWord[:i] + "*" + endWord[i+1:])

        queue = deque()
        queue.append(beginWord)

        count = 0

        visited = set()

        while queue:
            count += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return count
                for i in range(l):
                    pattern = word[:i] + "*" + word[i+1:]
                    neighbors = tree[pattern]
                    for neighbor in neighbors:
                        if neighbor in visited:
                            continue
                        else:
                            visited.add(neighbor)
                            queue.append(neighbor)
        return 0
            