package main

import (
	"math/rand"
	"fmt"
)

var MAX_LEVEL = 5

type node struct {
	key   int
	value int
	next  []*node
}

type SkipList struct {
	level int
	head  *node
}

func newNode(level int, key int, value int) *node {
	nl := []*node{}
	for i := 0; i < level; i++ {
		nl = append(nl, nil)
	}
	return &node{key, value, nl}
}

func NewSkipList() *SkipList {
	return &SkipList{0, newNode(MAX_LEVEL, 0, 0)}
}

func random() int {
	k := 0
	r := rand.Int()
	for r%2 == 1 {
		k++
		r = rand.Int()
	}
	return k
}

func (sl *SkipList) Insert(key int, value int) {
	p := sl.head
	update := make([]*node, MAX_LEVEL)

	// Step 1: Find the correct position to insert the new node, and store the
	// information where the level is going down.
	for i := sl.level - 1; i >= 0; i-- {
		for q := p.next[i]; q != nil && q.value < value; {
			p = q
			q = p.next[i]
		}
		update[i] = p
	}

	if p != sl.head && value == p.value {
		fmt.Println("The value already exists in the list.", value)
		return
	}

	// Step 2: Calculate a random number as the level of new node
	// NOTE: take care of the cases in which the new level is greater than the
	// current level of skip list.
	k := random()
	if k >= MAX_LEVEL {
		k = MAX_LEVEL - 1
	}
	if k >= sl.level {
		for i := k; i >= sl.level; i-- {
			update[i] = sl.head
		}
		sl.level = k + 1
	}

	// Step 3: Update the pointers
	q := newNode(k+1, key, value)

	for i := 0; i <= k; i++ {
		q.next[i] = update[i].next[i]
		update[i].next[i] = q
	}
}

func (sl *SkipList) echo() {
	fmt.Printf("The skip list has %d level(s).\n", sl.level)
	for i := sl.level - 1; i >= 0; i-- {
		fmt.Printf("Level #%d: ", i)
		for p := sl.head.next[i]; p != nil; p = p.next[i] {
			fmt.Print(p.value, " -> ")
		}
		fmt.Println("NIL")
	}
}

// TODO add search and delete

func main() {
	sl := NewSkipList()
	sl.Insert(7, 7)
	sl.Insert(4, 4)
	sl.Insert(8, 8)
	sl.Insert(3, 3)
	sl.Insert(1, 1)
	sl.Insert(2, 2)
	sl.echo()
}
