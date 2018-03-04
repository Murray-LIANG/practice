package main

import (
	"fmt"
)

func isCharIn_1(a string, b string) bool {
	lenA := len(a)
	lenB := len(b)
	for i := 0; i < lenB; i++ {
		for j := 0; j < lenA; j++ {
			if b[i] == a[j] {
				break
			}
			if j == lenA - 1 {
				return false
			}
		}
	}
	return true
}

func isCharIn_2(a string, b string) bool {
	have := [26]int{}
	aSlice := []byte(a)
	bSlice := []byte(b)

	for i := 0; i < len(a); i++ {
		have[aSlice[i] - 65] = 1
	}
	for i := 0; i < len(b); i++ {
		if have[bSlice[i] - 65] != 1 {
			return false
		}
	}
	return true
}

func isCharIn_3(a string, b string) bool {
	hash := 0
	aSlice := []byte(a)
	bSlice := []byte(b)

	for i := 0; i < len(a); i++ {
		hash |= (1 << (aSlice[i] - 65))
	}

	for i := 0; i < len(b); i++ {
		if hash & (1 << (bSlice[i] - 65)) == 0 {
			return false
		}
	}
	return true
}

type tuple struct {
	a, b string
}

func main() {
	test_data := []tuple{{"ABC", "CDE"}, {"A", "A"}}

	for i := 0; i < len(test_data); i++ {
		a := test_data[i].a
		b := test_data[i].b
		fmt.Println("a: ", a)
		fmt.Println("b: ", b)
		fmt.Println("isCharIn_1: ", isCharIn_1(a, b))
		fmt.Println("isCharIn_2: ", isCharIn_2(a, b))
		fmt.Println("isCharIn_3: ", isCharIn_3(a, b))
	}
}
