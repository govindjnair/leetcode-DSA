class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]

        d["."] = "."

    def search(self, word: str) -> bool:
        d = self.trie
        for c in word:
            if c not in d:
                return False
            d = d[c]

        return "." in d

    def startsWith(self, word: str) -> bool:
        d = self.trie
        for c in word:
            if c not in d:
                return False
            d = d[c]

        return True


obj = Trie()
obj.insert("apple")
obj.insert("application")
print(obj.startsWith("ap"))
