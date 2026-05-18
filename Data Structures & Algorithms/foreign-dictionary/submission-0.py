from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        chars = set()
        for word in words:
            for ch in word:
                chars.add(ch)

        edges = defaultdict(list)
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            for j in range(len(w1)):
                if len(w2) <= j:
                    return ""
                elif w1[j] == w2[j]:
                    continue
                else:
                    edges[w1[j]].append(w2[j])
                    break

        self.edges = edges
        self.done = set()
        visiting = set()
        self.result = []

        for ch in chars:
            if self.dfs(ch, visiting):
                return ""

        self.result.reverse()
        return "".join(self.result)
        

    def dfs(self, ch: str, visiting: set[str]) -> bool:
        if ch in visiting:
            return True
        if ch in self.done:
            return False
        visiting.add(ch)
        for child in self.edges[ch]:
            if self.dfs(child, visiting):
                return True
        visiting.remove(ch)
        self.done.add(ch)
        self.result.append(ch)
        return False
        