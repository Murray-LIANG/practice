package main

import "fmt"

func distance(p1 []int, p2 []int) int {
	return (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])
}

func validSquare(p1 []int, p2 []int, p3 []int, p4 []int) bool {
	tmp := map[int]int{}
	tmp[distance(p1, p2)] = 1
	tmp[distance(p1, p3)] = 1
	tmp[distance(p1, p4)] = 1
	tmp[distance(p2, p3)] = 1
	tmp[distance(p2, p4)] = 1
	tmp[distance(p3, p4)] = 1
	if _, ok := tmp[0]; !ok && len(tmp) == 2 {
		return true
	}
	return false
}

func main() {
	p1 := []int{0, 1}
	p2 := []int{2, 1}
	p3 := []int{1, 0}
	p4 := []int{1, 2}
	fmt.Println("Test data:", p1, p2, p3, p4)
	fmt.Println(validSquare(p1, p2, p3, p4))
}
