package main

import "fmt"

func trap(height []int) int {
	// The thought is to check how height water can be trapped on Xi (0 <= i <= n-1)
	// It is decided by the case there are bars from both sides (left/right)
	// higher than Xi, maybe they are not by Xi. And
	// the amount of water is min(leftHeight, rightHeight) - XiHeight.

	// There is a solution to scan the list twice, once for getting the exactly
	// nearest left Xj higher than Xi, the other one for getting the exactly
	// nearest right Xk higher than Xi. Of course these (Xj, Xk) pairs for each
	// Xi are stored in a list.

	// However, there is no need to scan twice, and spend so many space to
	// store Xj, Xk pair. Once there are higher bars from the left and right
	// side of Xi, no matter how far they are from Xi. The water will always be
	// trapped. We start from index 0 (i) and index n-1 (j), and keep the
	// record of max height of left (lmax), right (rmax). For each Xi, if rmax
	// is higher than it, its water will be trapped. Likewise, For each Xj, if
	// lmax is higher than it, its water will be trapped.

	n := len(height)
	i, j := 0, n-1
	lmax, rmax := 0, 0
	sum := 0
	for i < j {
		lmax = max(height[i], lmax)
		rmax = max(height[j], rmax)
		if lmax <= rmax {
			sum += lmax - height[i]
			i++
		} else {
			sum += rmax - height[j]
			j--
		}
	}
	return sum
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	data := []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
	fmt.Println(trap(data))
}
