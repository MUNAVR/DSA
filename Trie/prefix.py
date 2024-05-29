class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    

# Example usage:
trie = Trie()
trie.insert("cat")
trie.insert("car")
trie.insert("dog")
trie.insert("dot")

print(trie.search("cat"))  # Output: True
print(trie.search("can"))  # Output: False
print(trie.starts_with("do"))  # Output: True
print(trie.starts_with("c"))  # Output: True
print(trie.starts_with("ba"))  # Output: False


class TrieNode:
    def __init__(self) -> None:
        self.chil={}
        self.end_of_word=False
    
class Trie:
    def __init__(self) -> None:
        self.root=TrieNode()
    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.chil:
                node.chil[char]=TrieNode()
            node=node.chil[char]
        node.end_of_word=True
    def search(self,word):
        node=self.root
        for char in word:
            if char not in node.chil:
                return False
            node=node.chil[char]
        return node.end_of_word
    def start_with(self,prefix):
        node=self.root
        for char in prefix:
            if char not in node.chil:
                return False
            node=node.chil[char]
        return True
    


