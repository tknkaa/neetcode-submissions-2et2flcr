class WordDictionary:

    def __init__(self):
        self.root = {}
        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["#"] = True
        

    def search(self, word: str) -> bool:
        node = self.root
        i = 0
        for i in range(len(word)):
            c = word[i]
            if c == ".":
                for key in node:
                    if key == "#":
                        continue
                    new_word = word[:i] + key + word[i+1:]
                    if self.search(new_word):
                        return True
                return False
            elif c not in node:
                return False
            else:
                node = node[c]
        if "#" in node and node["#"]:
            return True
        else:
            return False
                
        
