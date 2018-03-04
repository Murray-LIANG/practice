package main

import "fmt"

func fourSumCount(A []int, B []int, C []int, D []int) int {
	sumAB := map[int]int{}
	for _, a := range A {
		for _, b := range B {
			sumAB[a+b]++
		}
	}
	result := 0
	for _, c := range C {
		for _, d := range D {
			result += sumAB[-c-d]
		}
	}
	return result
}

func main() {
	A := []int{-1,-1}
	B := []int{-1,1}
	C := []int{-1,1}
	D := []int{1,-1}
	fmt.Println(fourSumCount(A, B, C, D))
}
