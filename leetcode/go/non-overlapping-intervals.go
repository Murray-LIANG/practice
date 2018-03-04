package main

import (
	"sort"
	"math"
	"fmt"
)

/*
https://leetcode.com/problems/non-overlapping-intervals
 */

type Interval struct {
	Start int
	End   int
}

type IntervalSlice []Interval

func (s IntervalSlice) Less(i int, j int) bool {
	return s[i].End < s[j].End
}

func (s IntervalSlice) Swap(i int, j int) {
	s[i], s[j] = s[j], s[i]
}

func (s IntervalSlice) Len() int {
	return len(s)
}

func eraseOverlapIntervals(intervals []Interval) int {
	sort.Sort(IntervalSlice(intervals))
	fmt.Println(intervals)
	count := 0
	end := math.MinInt32
	for _, interval := range intervals {
		if interval.Start < end {
			count++
		} else {
			end = interval.End
		}
	}
	return count
}

func main() {
	fmt.Println(eraseOverlapIntervals([]Interval{{1, 2}, {2, 3, }, {3, 4}, {1, 3}}))
}
