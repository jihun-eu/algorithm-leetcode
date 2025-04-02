class Word:
    def __init__(self, char: str = ""):
        self.char = char
        self.endable = False
        self.next = {}

class WordDictionary:

    def __init__(self):
        self.wordDict = Word()

    def addWord(self, word: str) -> None:
        ptr = self.wordDict
        for char in word:            
            if char not in ptr.next:
                ptr.next[char] = Word(char)
            ptr = ptr.next[char]
        ptr.endable = True

    def search(self, word: str) -> bool:
        def _check(ptr: Word, idx: int) -> bool:
            nonlocal word
            if idx == len(word):
                return ptr.endable

            nextIdx = idx + 1
            char = word[idx]
            if char == ".":
                for nxt in ptr.next.values():
                    if _check(nxt, nextIdx):
                        return True

            if char not in ptr.next:
                return False
            
            return _check(ptr.next[char], nextIdx)

        ptr = self.wordDict
        return _check(ptr, 0)
        
        



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)