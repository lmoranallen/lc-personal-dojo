
# a Trie/Tree is made up of nodes so the particular node must be defined as well. 
class TrieNode:

    def __init__(self):
        self.children = {} # optimisations can be performed via hash-map
        self.endOfWord = False # end condition 

    
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        current = self.root 
        for c in word:
            if c not in current.children: 
                current.children[c] = TrieNode()
            current = current.children[c]
        current.endOfWord = True
    
    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.endOfWord


    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True

    


### Example: 

# insert('cat')

# c = 'c'
# curr.children = {}
# curr = TrieNode({'c': TrieNode()}, False)
# c = 'a'
# c = 't'
# Final Shape:
# 
#    curr = TrieNode(
#       {'c': TrieNode(
#         {'a': TrieNode(
#           {'t': TrieNode({}), True}
#        ), False}
#      ), False}
#
#
# Each character is a node traversing BFS from an empty string to a given prefix
# earch and startsWith are the same except for a given prefix 
#
# 
# 
# 
# )}, False)