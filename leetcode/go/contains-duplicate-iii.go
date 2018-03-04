package main

import (
	"math"
	"fmt"
)

/*
https://leetcode.com/problems/contains-duplicate-iii

|nums[i] - nums[j]| <= t
|i - j| <= k
That is two numbers in nums, their distance is no more than t, while their
indexes distance is no more than k.
So we could think that putting the numbers whose distance is no more than t in
the same bucket, that is, there are at most t+1 numbers in one bucket (Of
course there are no more than two number in the same bucket in this problem).
For index distance, k is the max count of buckets because the index with distance
more than k doesn't meet the requirement any more, we could delete it. For
example, considering we are checking number on index I OCP, if I - 0 > k, then
the bucket having number of index 0 isn't needed any more.

Take nums = [3, 0 , 6, 9], k = 3, t = 2 as example,
the buckets are like: (0, 1, 2), (3, 4, 5), (6, 7, 8). For I = 0, nums[I] = 3,
putting it in the second bucket, then B1 = 3, for I = 1, nums[I] = 0, putting
it in the first bucket, then B0 = 0, need to check the number in B0 with B0's
adjacent bucket B1, to see the distance of number would be no more than t.
 */

func containsNearbyAlmostDuplicate(nums []int, k int, t int) bool {
	if k <= 0 || t <= -1 {
		return false
	}
	buckets := map[int64]int{}
	for i, num := range nums {
		tempNum := num - math.MinInt32
		bucketNo := int64(tempNum / (t + 1))
		if _, ok := buckets[bucketNo]; ok {
			return true
		}
		if preNum, ok := buckets[bucketNo-1]; ok && tempNum-preNum <= t {
			return true
		}
		if nextNum, ok := buckets[bucketNo+1]; ok && nextNum-tempNum <= t {
			return true
		}

		if len(buckets) == k {
			delete(buckets, int64((nums[i-k]-math.MinInt32)/(t+1)))
		}
		buckets[bucketNo] = tempNum
	}
	return false
}

func main() {
	fmt.Println(containsNearbyAlmostDuplicate([]int{3, 6, 9, 0}, 3, 2))
	fmt.Println(containsNearbyAlmostDuplicate([]int{-1, -1}, 1, -1))
}
