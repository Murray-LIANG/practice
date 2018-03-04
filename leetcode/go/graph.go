package main

import "fmt"

type vertexNode struct {
	name string
	info string
}

type adjacencyNode struct {
	id   int
	next *adjacencyNode
}

type tableNode struct {
	vertex        *vertexNode
	adjacencyList *adjacencyNode
	indegree      int
}

type graph struct {
	table   []tableNode
	mapping map[string]int
}

func (g graph) topSort() []*vertexNode {
	result := []*vertexNode{}
	queue := []int{}
	for i := 1; i < len(g.table); i++ {
		if g.table[i].indegree == 0 {
			queue = append(queue, i)
		}
	}
	for len(queue) != 0 {
		i := queue[0]
		result = append(result, g.table[i].vertex)
		fmt.Println("Found:", g.table[i].vertex.name)
		queue = queue[1:]
		for adjacency := g.table[i].adjacencyList; adjacency != nil;
		adjacency = adjacency.next {
			fmt.Println("Check adjacency:", adjacency.id)
			g.table[adjacency.id].indegree--
			if g.table[adjacency.id].indegree == 0 {
				queue = append(queue, adjacency.id)
			}
		}
	}
	return result
}

func main() {
	g := graph{make([]tableNode, 8), map[string]int{}}
	v1 := vertexNode{"Node #1", "Info #1"}
	v2 := vertexNode{"Node #2", "Info #2"}
	v3 := vertexNode{"Node #3", "Info #3"}
	v4 := vertexNode{"Node #4", "Info #4"}
	v5 := vertexNode{"Node #5", "Info #5"}
	v6 := vertexNode{"Node #6", "Info #6"}
	v7 := vertexNode{"Node #7", "Info #7"}
	a13 := adjacencyNode{3, nil}
	a12 := adjacencyNode{4, &a13}
	a11 := adjacencyNode{2, &a12}
	g.table[1] = tableNode{&v1, &a11, 0}
	g.mapping[v1.name] = 1
	a22 := adjacencyNode{5, nil}
	a21 := adjacencyNode{4, &a22}
	g.table[2] = tableNode{&v2, &a21, 1}
	g.mapping[v2.name] = 2
	a31 := adjacencyNode{6, nil}
	g.table[3] = tableNode{&v3, &a31, 2}
	g.mapping[v3.name] = 3
	a43 := adjacencyNode{3, nil}
	a42 := adjacencyNode{7, &a43}
	a41 := adjacencyNode{6, &a42}
	g.table[4] = tableNode{&v4, &a41, 3}
	g.mapping[v4.name] = 4
	a52 := adjacencyNode{7, nil}
	a51 := adjacencyNode{4, &a52}
	g.table[5] = tableNode{&v5, &a51, 1}
	g.mapping[v5.name] = 5
	g.table[6] = tableNode{&v6, nil, 3}
	g.mapping[v6.name] = 6
	a71 := adjacencyNode{6, nil}
	g.table[7] = tableNode{&v7, &a71, 2}
	g.mapping[v7.name] = 7

	result := g.topSort()
	for i := 0; i < len(result); i++ {
		fmt.Println(result[i].name)
	}
}

