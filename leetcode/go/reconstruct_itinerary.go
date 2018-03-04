package main

import (
	"sort"
	"fmt"
)

/*
 * https://leetcode.com/problems/reconstruct-itinerary
 * Eulerian path, use DFS.
 * Starting JFK, visits the airports using DFS until the one (denoted as Z)
 * having no out ticket.
 * Use recursion, it will recheck the previous airport (W) of Z, to see if
 * there are still tickets to other airports besides Z. then enter another
 * recursion.
 */

func findItinerary(tickets [][]string) []string {
	targets := map[string][]string{}
	for _, tuple := range tickets {
		if _, ok := targets[tuple[0]]; ok {
			targets[tuple[0]] = append(targets[tuple[0]], tuple[1])
		} else {
			targets[tuple[0]] = []string{tuple[1]}
		}
	}
	for _, v := range targets {
		sort.Sort(sort.StringSlice(v))
	}
	stack := []string{}
	var visit func(string)
	visit = func(airport string) {
		for len(targets[airport]) != 0 {
			next := targets[airport][0]
			targets[airport] = targets[airport][1:]
			visit(next)
		}
		stack = append(stack, airport)
	}
	visit("JFK")
	fmt.Println(stack)
	return reverse(stack)

}

func reverse(s []string) []string {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
	return s
}

func main() {
	tickets := [][]string{
		{"JFK", "A"}, {"JFK", "D"}, {"A", "C"}, {"B", "C"},
		{"C", "D"}, {"C", "JFK"}, {"D", "A"}, {"D", "B"}}
	fmt.Println(findItinerary(tickets))
}
