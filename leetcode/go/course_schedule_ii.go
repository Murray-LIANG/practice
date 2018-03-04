package main

import (
	"container/list"
	"fmt"
)

func newGraphBFS(numCourses int, prerequisites [][]int) ([]int, map[int][]int) {
	incomingNums := make([]int, numCourses)
	courseGraph := make(map[int][]int, numCourses)

	for _, pair := range prerequisites {
		incomingNums[pair[0]]++
		courseGraph[pair[1]] = append(courseGraph[pair[1]], pair[0])
	}
	return incomingNums, courseGraph
}

func byBFS(incomingNums []int, courseGraph map[int][]int) []int {
	toVisit := list.New()
	for index, num := range incomingNums {
		if num == 0 {
			toVisit.PushBack(index)
		}
	}
	visited := 0
	result := []int{}
	for toVisit.Len() > 0 {
		course := toVisit.Front()
		visited++
		result = append(result, course.Value.(int))
		toVisit.Remove(course)
		for _, nextCourse := range courseGraph[course.Value.(int)] {
			incomingNums[nextCourse]--
			if incomingNums[nextCourse] == 0 {
				toVisit.PushBack(nextCourse)
			}
		}
	}
	if visited == len(incomingNums) {
		return result
	} else {
		return []int{}
	}
}

func newGraphDFS(numCourses int, prerequisites [][]int) ([]int, map[int][]int) {
	fanOutNums := make([]int, numCourses)
	courseGraph := make(map[int][]int, numCourses)

	for _, pair := range prerequisites {
		fanOutNums[pair[1]]++
		courseGraph[pair[0]] = append(courseGraph[pair[0]], pair[1])
	}
	return fanOutNums, courseGraph
}

func byDFS(fanOutNums []int, courseGraph map[int][]int) []int {
	stack := list.New()
	for index, num := range fanOutNums {
		if num == 0 {
			stack.PushBack(index)
		}
	}
	visited := 0
	result := list.New()
	for stack.Len() > 0 {
		course := stack.Back()
		visited++
		result.PushFront(course.Value)
		stack.Remove(course)
		for _, preCourse := range courseGraph[course.Value.(int)] {
			fanOutNums[preCourse]--
			if fanOutNums[preCourse] == 0 {
				stack.PushBack(preCourse)
			}
		}
	}
	if visited == len(fanOutNums) {
		tmp := []int{}
		for it := result.Front(); it != nil; it = it.Next() {
			tmp = append(tmp, it.Value.(int))
		}
		return tmp
	} else {
		return []int{}
	}
	return []int{}
}

func findOrder(numCourses int, prerequisites [][]int) []int {
	//incomingNums, courseGraph := newGraphBFS(numCourses, prerequisites)
	//return byBFS(incomingNums, courseGraph)
	fanOutNums, courseGraph := newGraphDFS(numCourses, prerequisites)
	return byDFS(fanOutNums, courseGraph)
}

func main() {
	data := [][]int{{1, 0}, {2, 0}, {3, 1}, {3, 2}}

	fmt.Println(findOrder(4, data))
}
