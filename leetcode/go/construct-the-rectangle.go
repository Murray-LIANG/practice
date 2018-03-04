package main

import (
	"math"
	"fmt"
)

/*
https://leetcode.com/problems/construct-the-rectangle
 */

func constructRectangle(area int) []int {
	n := math.Sqrt(float64(area))
	t := int(math.Ceil(n))
	for area % t != 0 {t++}
	return []int{t, area/t}
}

func main() {
	fmt.Println(constructRectangle(4))
	fmt.Println(constructRectangle(8))
	fmt.Println(constructRectangle(12))
	fmt.Println(constructRectangle(13))
}
