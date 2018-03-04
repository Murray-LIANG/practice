package main

import (
	"fmt"
	"strconv"
	"strings"
)

func canIWin(maxChoosableInteger int, desiredTotal int) bool {
	sum := maxChoosableInteger * (maxChoosableInteger + 1) / 2
	if sum < desiredTotal {
		return false
	}
	choosables := []int{}
	for i := 1; i <= maxChoosableInteger; i++ {
		choosables = append(choosables, i)
	}
	memo := map[string]bool{}
	win, _ := canCaseWin(choosables, desiredTotal, memo)
	return win
}

func canCaseWin(choosables []int, desiredTotal int,
				memo map[string]bool) (bool, map[string]bool) {

	s := format(choosables)
	if ok, value := memo[s]; ok {
		return value, memo
	}
	if choosables[len(choosables)-1] >= desiredTotal {
		return true, memo
	}

	for i := 0; i < len(choosables); i++ {
		new_choosables := []int{}
		new_choosables = append(new_choosables, choosables[:i]...)
		new_choosables = append(new_choosables, choosables[i+1:]...)
		// If the competitor cannot win after I choose any number from
		// `choosables`, then I win.
		if win, new_memo := canCaseWin(new_choosables,
									   desiredTotal-choosables[i],
									   memo); !win {
			new_memo[s] = true
			return true, new_memo
		}
	}
	memo[s] = false
	return false, memo
}

func format(nums []int) string {
	s := []string{}
	for _, n := range nums {
		s = append(s, strconv.Itoa(n))
	}
	return strings.Join(s, "")
}

func main() {
	data := []int{10, 40}
	fmt.Println(canIWin(data[0], data[1]))
}
