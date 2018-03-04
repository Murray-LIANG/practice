package main

import "fmt"

func nextGreaterElement(findNums []int, nums []int) []int {
	result := []int{}
	tmpMap := genMap(nums)
	for i := 0; i < len(findNums); i++ {
		value, ok := tmpMap[findNums[i]]
		if ok {
			result = append(result, value)
		} else {
			result = append(result, -1)
		}
	}
	return result
}

func genMap(elements []int) map[int]int {
	result := map[int]int{}
	stack := []int{}
	for i := 0; i < len(elements); i++ {
		for len(stack) > 0 && stack[len(stack) - 1] < elements[i] {
			element := stack[len(stack) - 1]
			stack = stack[:len(stack) - 1]
			result[element] = elements[i]
		}
		stack = append(stack, elements[i])
	}
	return result
}

func main() {
	sub := []int{1, 2, 3}
	all := []int{4, 2, 1, 2}
	fmt.Println(nextGreaterElement(sub, all))
}
