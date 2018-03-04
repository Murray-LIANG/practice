package main

import (
	"strconv"
)

/*
https://leetcode.com/problems/mini-parser
 */

// This is the interface that allows for creating nested lists.
// You should not implement it, or speculate about its implementation
type NestedInteger struct {
	isInteger bool
	integer   int
	list      []*NestedInteger
}

// Return true if this NestedInteger holds a single integer, rather than a nested list.
func (n NestedInteger) IsInteger() bool {
	return n.isInteger
}

// Return the single integer that this NestedInteger holds, if it holds a single integer
// The result is undefined if this NestedInteger holds a nested list
// So before calling this method, you should have a check
func (n NestedInteger) GetInteger() int {
	return n.integer
}

// Set this NestedInteger to hold a single integer.
func (n *NestedInteger) SetInteger(value int) {
	n.isInteger = true
	n.integer = value
}

// Set this NestedInteger to hold a nested list and adds a nested integer to it.
func (n *NestedInteger) Add(elem NestedInteger) {
	n.isInteger = false
	n.list = append(n.list, &elem)
}

// Return the nested list that this NestedInteger holds, if it holds a nested list
// The list length is zero if this NestedInteger holds a single integer
// You can access NestedInteger's List element directly if you want to modify it
func (n NestedInteger) GetList() []*NestedInteger {
	return n.list
}

func deserialize(s string) *NestedInteger {
	res := &NestedInteger{}
	if len(s) == 0 {
		return res
	}
	if s[0] != '[' {
		num, _ := strconv.Atoi(s)
		res.SetInteger(num)
		return res
	} else {
		for i := 1; i < len(s)-1; {
			start := i
			if s[i] == '[' {
				countOpenBracket := 0
				for i < len(s)-1 {
					if s[i] == '[' {
						countOpenBracket++
					} else if s[i] == ']' {
						countOpenBracket--
					}
					i++
					if countOpenBracket == 0 {
						break
					}
				}
				res.Add(*deserialize(s[start:i]))
			} else {
				for i < len(s)-1 {
					if s[i] == ',' {
						break
					}
					i++
				}
				res.Add(*deserialize(s[start:i]))
			}
			i++
		}
		return res
	}
}

func main() {
	//deserialize("[123,[456,[789]]]")
	deserialize("[123,456,[788,799,833],[[]],10,[]]")
}
