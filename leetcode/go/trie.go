package main

import "fmt"

type Trie struct {
	word string
	kids map[byte]*Trie
}

func NewTrie() *Trie {
	trie := new(Trie)
	trie.kids = map[byte]*Trie{}
	return trie
}

/** Initialize your data structure here. */
func Constructor() Trie {
	return *NewTrie()
}


/** Inserts a word into the trie. */
func (this *Trie) Insert(word string) {
	tmpNode := this
	for _, c := range word {
		if tmpNode.kids[byte(c)] == nil {
			tmpNode.kids[byte(c)] = NewTrie()
		}
		tmpNode = tmpNode.kids[byte(c)]
	}
	tmpNode.word = word
}


/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
	tmpNode := this
	for _, c := range word {
		if tmpNode.kids[byte(c)] == nil {
			return false
		}
		tmpNode = tmpNode.kids[byte(c)]
	}
	return tmpNode.word == word
}


/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {
	tmpNode := this
	for _, c := range prefix {
		if tmpNode.kids[byte(c)] == nil {
			return false
		}
		tmpNode = tmpNode.kids[byte(c)]
	}
	return true
}


/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */

func main() {
	trie := Constructor()
	trie.Insert("hello")
	trie.Insert("liangr")
	fmt.Println("hello in Trie ?", trie.Search("hello"))
	fmt.Println("ryan in Trie ?", trie.Search("ryan"))
	fmt.Println("Any word starts with liang ?", trie.StartsWith("liang"))
	fmt.Println("Any word starts with hello ?", trie.StartsWith("hello"))
	fmt.Println("Any word starts with r ?", trie.StartsWith("r"))
}
