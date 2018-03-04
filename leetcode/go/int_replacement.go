package main

import "fmt"

func integerReplacement(n int) int {
	count := 0
	for n != 1 {
		if n & 1 == 0{
			n >>= 1
		} else if n == 3 || n >> 1 & 1 == 0 {
			n -= 1
		} else {
			n += 1
		}
		count++
	}
	return count
}

type TestData struct {
	input int
	expected int
}

func main() {
	datas := []TestData{
		{8, 3},
		{7, 4},
		{3, 2},
	}
	for _, data := range datas {
		fmt.Println("Input n:", data.input)
		result := integerReplacement(data.input)
		fmt.Println("Output:", result)
		fmt.Println("Result expected?", result == data.expected)
	}
}
