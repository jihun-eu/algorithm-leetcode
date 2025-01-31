class Trie:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        currTrie = self.trie
        for char in word:
            if char not in currTrie:
                currTrie[char] = {}
            currTrie = currTrie[char]
        currTrie['*'] = None
        

    def search(self, word: str) -> bool:
        currTrie = self.trie
        for char in word:
            if char not in currTrie:
                return False
            currTrie = currTrie[char]
        return '*' in currTrie
        

    def startsWith(self, prefix: str) -> bool:
        currTrie = self.trie
        for char in prefix:
            if char not in currTrie:
                return False
            currTrie = currTrie[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)