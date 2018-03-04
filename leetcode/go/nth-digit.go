package main

import (
	"strconv"
	"fmt"
)

/*
https://leetcode.com/problems/nth-digit
 */

func findNthDigit(n int) int {
	for i := 0; true; i++ {
		start := 1
		for k := i; k > 0; k-- {
			start *= 10
		}
		i9 := 9 * start * (i + 1)
		if n > i9 {
			n -= i9
			continue
		}
		nthNum := (n - 1) / (i + 1)
		nthNum = start + nthNum
		sNum := strconv.Itoa(nthNum)
		return (int)(sNum[(n-1)%(i+1)]) - '0'
	}
	return 0
}

func main() {
	fmt.Println(findNthDigit(9))
	fmt.Println(findNthDigit(10))
	fmt.Println(findNthDigit(11))
	fmt.Println(findNthDigit(12))
}
