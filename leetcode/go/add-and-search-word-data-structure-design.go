package main

import "fmt"

/*
https://leetcode.com/problems/add-and-search-word-data-structure-design

Use a Trie tree.
 */

type TrieNode struct {
	Children [26]*TrieNode
	Word     string
}

type WordDictionary struct {
	Root *TrieNode
}

/**
 * Initialize your data structure here.
 */
func Constructor() WordDictionary {
	return WordDictionary{&TrieNode{}}
}

/**
 * Adds a word into the data structure.
 */
func (this *WordDictionary) AddWord(word string) {
	node := this.Root
	for _, ch := range word {
		if node.Children[ch-'a'] == nil {
			node.Children[ch-'a'] = &TrieNode{}
		}
		node = node.Children[ch-'a']
	}
	node.Word = word
}

/**
 * Returns if the word is in the data structure. A word could contain the dot
 * character '.' to represent any one letter.
 */
func (this *WordDictionary) Search(word string) bool {
	var dfs func(*TrieNode, []byte) bool
	dfs = func(node *TrieNode, bytes []byte) bool {
		if len(bytes) == 0 {
			return len(node.Word) != 0
		}
		if bytes[0] == '.' {
			for _, child := range node.Children {
				if child != nil {
					if dfs(child, bytes[1:]) {
						return true
					}
				}
			}
		} else if node.Children[bytes[0]-'a'] != nil {
			return dfs(node.Children[bytes[0]-'a'], bytes[1:])
		}
		return false
	}
	return dfs(this.Root, []byte(word))
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */

func main() {
	dict := Constructor()
	dict.AddWord("abc")
	dict.AddWord("cbc")
	dict.AddWord("cec")
	fmt.Println(dict.Search("."))
	fmt.Println(dict.Search("ab"))
	fmt.Println(dict.Search("..."))
	fmt.Println(dict.Search("abcd"))
	fmt.Println(dict.Search("cec"))
}
