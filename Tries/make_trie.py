class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        r= self.root
        for char in word:
            if char not in r.children:
                r.children[char]=TrieNode()
            r=r.children[char]
        r.end=True


    def search(self, word: str) -> bool:
        r=self.root
        for char in word:
            if char not in r.children:
                return False
            r=r.children[char]
        return r.end
        

    def startsWith(self, prefix: str) -> bool:
        r=self.root
        for char in prefix:
            if char not in r.children:
                return False
            r=r.children[char]
        return True
        
        