package main

import "fmt"

type node struct {
	key int
	children []*node
}

func NewNode() *node {
	return &node{}
}


func main() {
	n := node{}
	s := []*node{}
	if s == nil {
		fmt.Println("s is nil.")
	} else {
		fmt.Println("s is not nil, ", s)
	}

	var t []int
	if t == nil {
		fmt.Println("t is nil.")
	}
	t = append(t, 0)
	fmt.Println("t:", t)

	//var abc int
	//abc = nil
	//fmt.Println("abc: ", abc)

	fmt.Println(len(n.children))
	n.children = append(n.children, &node{})
	fmt.Println(len(n.children))
	if n.children == nil {
		fmt.Println("Children is nil.")
	} else {
		fmt.Println("Children is not nil, ", n.children)
	}
}
