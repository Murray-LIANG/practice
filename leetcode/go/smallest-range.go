package main

import (
	"container/heap"
	"math"
	"fmt"
)

/*
https://leetcode.com/problems/smallest-range
 */

type Element struct {
	Val     int
	Index   int
	ArrayNo int
}

type Elements []*Element

func (el *Elements) Push(e interface{}) {
	*el = append(*el, e.(*Element))
}

func (el *Elements) Pop() interface{} {
	n := len(*el)
	if n > 0 {
		x := (*el)[n-1]
		*el = (*el)[:n-1]
		return x
	}
	return nil
}

func (el *Elements) Len() int {
	return len(*el)
}

func (el *Elements) Less(i, j int) bool {
	return (*el)[i].Val < ((*el)[j]).Val
}

func (el *Elements) Swap(i, j int) {
	(*el)[i], (*el)[j] = (*el)[j], (*el)[i]
}

func smallestRange(nums [][]int) []int {
	var max func(int, int) int
	max = func (a, b int) int {
		if a < b {
			return b
		}
		return a
	}

	el := (*Elements)(new([]*Element))
	heap.Init(el)

	right := math.MinInt32
	for arrayNo, array := range nums {
		right = max(right, array[0])
		heap.Push(el, &Element{array[0], 0, arrayNo})
	}
	minRange := right - (*el)[0].Val
	minLeft := (*el)[0].Val

	for true {
		e := *(heap.Pop(el).(*Element))
		array := nums[e.ArrayNo]
		if e.Index == len(array) -1 {
			break
		}
		right = max(right, array[e.Index+1])
		heap.Push(el, &Element{array[e.Index+1], e.Index+1, e.ArrayNo})
		if minRange > right-(*el)[0].Val {
			minRange = right-(*el)[0].Val
			minLeft = (*el)[0].Val
		}
	}
	return []int{minLeft, minLeft +minRange}
}

func main() {
	fmt.Println(smallestRange([][]int{{4,10,15,24,26}, {0,9,12,20}, {5,18,22,30}}))
}
