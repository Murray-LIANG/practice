package main

import (
	"strings"
	"fmt"
	"strconv"
)

/*
https://leetcode.com/problems/basic-calculator
 */

func calculate(s string) int {
	s = strings.Replace(s, " ", "", -1)
	nums := []int{}
	op := []byte{}
	priority := map[byte]int{'(': 0, '-': 1, '+': 1, ')': 2}

	var popAndCalc func()
	popAndCalc = func() {
		topOp := op[len(op)-1]
		op = op[:len(op)-1]
		op1 := nums[len(nums)-2]
		op2 := nums[len(nums)-1]
		nums = nums[:len(nums)-2]
		if topOp == '+' {
			nums = append(nums, op1+op2)
		} else {
			nums = append(nums, op1-op2)
		}
	}

	for i := 0; i < len(s); {
		ch := s[i]
		numEnd := i
		for ch >= '0' && ch <= '9' {
			numEnd++
			if numEnd == len(s) {
				break
			}
			ch=s[numEnd]
		}
		if numEnd != i {
			num, _ := strconv.Atoi(s[i:numEnd])
			nums = append(nums, num)
			i = numEnd
		} else {
			i++
			if ch == ')' {
				for op[len(op)-1] != '(' {
					popAndCalc()
				}
				op = op[:len(op)-1] // remove the '('
			} else if ch == '(' || len(op) == 0 || priority[ch] > priority[op[len(op)-1]] {
				op = append(op, ch)
			} else {
				popAndCalc()
				op = append(op, ch)
			}
		}
	}
	for len(op) != 0 {
		popAndCalc()
	}
	return nums[0]
}

func main() {
	fmt.Println(calculate("(1+(4+5+2)-3)+(6+8)"))
	fmt.Println(calculate("2147483647"))
	fmt.Println(calculate("999+1"))
}
