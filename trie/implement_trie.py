class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word.lower():
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr['*'] = ''

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word.lower():
            if ch not in curr:
                return False
            curr = curr[ch]
        return '*' in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix.lower():
            if ch not in curr:
                return False
            curr = curr[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
