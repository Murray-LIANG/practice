package main

import "fmt"

/*
https://leetcode.com/problems/valid-perfect-square
 */

func isPerfectSquare(num int) bool {
	for low, high := 1, num; low < high; {
		mid := (low + high) / 2
		midSquared := mid * mid
		if midSquared== num {
			return true
		} else if midSquared < num {
			low = mid + 1
		} else {
			high = mid -1
		}
	}
	return false
}

func main() {
	fmt.Println(isPerfectSquare(9))
	fmt.Println(isPerfectSquare(10))
	fmt.Println(isPerfectSquare(11))
	fmt.Println(isPerfectSquare(12))
	fmt.Println(isPerfectSquare(13))
	fmt.Println(isPerfectSquare(14))
	fmt.Println(isPerfectSquare(15))
	fmt.Println(isPerfectSquare(16))
}
