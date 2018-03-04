package main

import (
	"strconv"
	"fmt"
	"math"
)

/*
https://leetcode.com/problems/next-greater-element-iii
 */

func nextGreaterElement(n int) int {
	s := []byte(strconv.Itoa(n))
	i:=len(s)-2
	for ; i >= 0; i-- {
		if s[i] < s[i+1] {
			break
		}
	}
	if i == -1 {
		return -1
	}
	j := len(s) -1
	for ; j >= i; j-- {
		if s[j] > s[i] {
			break
		}
	}
	s[i], s[j] = s[j], s[i]
	for p, q :=i+1, len(s)-1; p < q; p++ {
		s[p], s[q] = s[q], s[p]
		q--
	}

	res, _ := strconv.Atoi(string(s))
	if res <= math.MaxInt32 {
		return res
	} else {
		return -1
	}
}

func main() {
	fmt.Println(nextGreaterElement(534976))
	fmt.Println(nextGreaterElement(5341))
	fmt.Println(nextGreaterElement(5431))
	fmt.Println(nextGreaterElement(12443322))
	fmt.Println(nextGreaterElement(1999999999))
}
