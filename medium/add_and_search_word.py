import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end_of_word = False
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for char in word:
            node = node.children[char]
        node.end_of_word = True
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res
    def dfs(self, node, word):
        if not word:
            if node.end_of_word == True:
                self.res = True
            return
        if word[0] == ".":
            for node in node.children.values():
                self.dfs(node,word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])
