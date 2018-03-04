//
// Created by liangr on 9/1/17.
//

// https://leetcode.com/problems/implement-trie-prefix-tree

#include <string>
#include <vector>

using namespace std;

class TrieNode {
public:
    vector<TrieNode *> children;
    bool isWord;

    TrieNode(bool isWord = false) : isWord(isWord), children(26, NULL) {
    }
};

class Trie {
public:
    /** Initialize your data structure here. */
    Trie() : root(new TrieNode()) {
    }

    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode *node = root;
        for (auto ch: word) {
            int index = ch - 'a';
            if (node->children[index] == NULL) {
                node->children[index] = new TrieNode();
            }
            node = node->children[index];
        }
        node->isWord = true;
    }

    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode *node = find(word);
        return node != NULL && node->isWord;
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        TrieNode *node = find(prefix);
        return node != NULL;
    }

private:
    TrieNode *root;

    TrieNode* find(string key) {
        TrieNode *node = root;
        for (auto ch: key) {
            int index = ch - 'a';
            if (node->children[index] == NULL) {
                return NULL;
            }
            node = node->children[index];
        }
        return node;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * bool param_2 = obj.search(word);
 * bool param_3 = obj.startsWith(prefix);
 */
