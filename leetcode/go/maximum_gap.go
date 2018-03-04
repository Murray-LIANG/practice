package main

import (
	"math"
	"fmt"
)

/*
https://leetcode.com/problems/maximum-gap

The basic solution is to sort the list first, then traverse it one item by one.
This solution is O(nlogn) at least.

We need to use O(n) sort to improve it. Bucket sort is the one. The O(n)
solution is that 1) scan the list once and get the min and max value in the
list. We know that the max gap >= (max - min) / (n-1) (ie. [1,3,5,7,9,11]),
so if we put all the numbers into (n-1) buckets, then the two numbers
with the max gap will not be in the same buckets. And we only need to store
only two numbers for each buckets, one for the max number exists in the bucket,
another for the min number. Finally, we traverse the buckets one by one, the
max gap must be in the gaps of current bucket's min number minus the previous
bucket's max number.
 */

func maximumGap(nums []int) int {
	n := len(nums)
	if n <= 1 {
		return 0
	}
	min, max := nums[0], nums[0]
	for _, num := range nums {
		if num < min {
			min = num
		}
		if num > max {
			max = num
		}
	}
	bucketCount := n - 1
	bucketGap := int(math.Ceil(float64(max-min) / float64(bucketCount)))
	buckets := make([][]int, bucketCount)
	for _, num := range nums {
		if num == max {
			continue
		}
		index := (num - min) / bucketGap
		if buckets[index] == nil {
			buckets[index] = []int{num, num}
		} else if num < buckets[index][0] {
			buckets[index][0] = num
		} else if num > buckets[index][1] {
			buckets[index][1] = num
		}
	}
	res, pre := math.MinInt32, min
	for _, minMax := range buckets {
		if minMax != nil {
			if minMax[0]-pre > res {
				res = minMax[0] - pre
			}
			pre = minMax[1]
		}
	}
	if max-pre > res {
		res = max - pre
	}
	return res
}

func main() {
	//fmt.Println(maximumGap([]int{4, 1, 8, 9, 7, 11}))
	//fmt.Println(maximumGap([]int{4, 1, 8, 7, 11}))
	//fmt.Println(maximumGap([]int{1, 100}))
	fmt.Println(maximumGap([]int{1, 1, 1, 1, 1, 5, 5, 5, 5, 5}))
}
