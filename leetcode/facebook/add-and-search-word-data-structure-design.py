"""
https://leetcode.com/problems/add-and-search-word-data-structure-design
"""


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.trie_root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the
        dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        def _helper(node, word):
            if not word:
                return node.is_word
            if word[0] == '.':
                return any(_helper(child, word[1:])
                           for child in node.children.values())
            if word[0] not in node.children:
                return False
            else:
                return _helper(node.children[word[0]], word[1:])

        return _helper(self.trie_root, word)



d = WordDictionary()
d.addWord('bad')
d.addWord('dad')
d.addWord('mad')
print(d.search('dad'))
print(d.search('..d'))
print(d.search('m.f'))

