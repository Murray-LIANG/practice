package main

import (
	"strconv"
	"fmt"
)

/*
https://leetcode.com/problems/different-ways-to-add-parentheses
 */

func diffWaysToCompute(input string) []int {

	res := []int{}
	for index, ch := range input {
		if byte(ch) == '+' || byte(ch) == '-' || byte(ch) == '*' {
			leftSlice := diffWaysToCompute(input[:index])
			rightSlice := diffWaysToCompute(input[index+1:])
			for _, left := range leftSlice {
				for _, right := range rightSlice {
					subRes := 0
					if byte(ch) == '+' {
						subRes = left + right
					} else if byte(ch) == '-' {
						subRes = left - right
					} else {
						subRes = left * right
					}
					res = append(res, subRes)
				}
			}
		}
	}
	if len(res) == 0 {
		// this is the boundary condition, means the input string doesn't
		// contain any operators.
		v, _ := strconv.Atoi(input)
		res = append(res, v)
	}
	return res
}

func main() {
	fmt.Println(diffWaysToCompute("2*3-4*5"))
}
