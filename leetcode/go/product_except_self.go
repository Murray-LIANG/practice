package main

import (
	"fmt"
	"reflect"
)

func productExceptSelf_2nSpace(nums []int) []int {
	n := len(nums)
	fromHead := make([]int, n)
	fromTail := make([]int, n)
	fromHead[0], fromTail[n - 1] = 1, 1
	for i := 1; i < n; i++ {
		fromHead[i] = fromHead[i - 1] * nums[i - 1]
		fromTail[n - i - 1] = fromTail[n - i] * nums[n - i]
	}
	result := make([]int, n)
	for i := 0; i < n; i++ {
		result[i] = fromHead[i] * fromTail[i]
	}
	return result
}

func productExceptSelf(nums []int) []int {
	n := len(nums)
	result := make([]int, n)
	for i := 0; i < n; i++ {
		result[i] = 1
	}
	fromHead, fromTail := 1, 1
	for i := 1; i < n; i++ {
		fromHead *= nums[i - 1]
		result[i] *= fromHead
		fromTail *= nums[n - i]
		result[n - i - 1] *= fromTail
	}
	return result
}

type TestData struct {
	input    []int
	expected []int
}

func main() {
	datas := []TestData{{[]int{1, 2, 3, 4}, []int{24, 12, 8, 6}}}
	for index, data := range datas {
		fmt.Printf("Test Round #%d\n", index)
		fmt.Println("Input nums:", data.input)
		result2nSpace := productExceptSelf_2nSpace(data.input)
		fmt.Println("Output result of 2N space algorithm:",
			result2nSpace)
		fmt.Println("Expected ?", reflect.DeepEqual(result2nSpace,
			data.expected))
		fmt.Println("------------------------------------------")
		result := productExceptSelf(data.input)
		fmt.Println("Output result of N space algorithm:", result)
		fmt.Println("Expected ?", reflect.DeepEqual(result,
			data.expected))
		fmt.Println()
	}
}
