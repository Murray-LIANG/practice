class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

    def __repr__(self):
        return '{}. Children: {}.'.format(self.is_word, self.children)

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True

if __name__ == '__main__':
    t = Trie()
    print(t.search('a'))
    print(t.startsWith('a'))
    t.insert('a')
    t.insert('abc')
    #t.insert('ab')

    print(t.search('ab'))
    print(t.search('abc'))

    print(t.startsWith('ab'))
    print(t.startsWith('abc'))
