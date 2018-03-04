package main

import "fmt"

func LeftShiftOne(s []byte) {
	if len(s) == 0 {
		return
	}
	t := s[0]
	for i := 1; i < len(s); i++ {
		s[i - 1] = s[i]
	}
	s[len(s) - 1] = t
}

func LeftShiftM_1(s []byte, m int) {
	m %= len(s)
	for m > 0 {
		LeftShiftOne(s)
		m--
	}
}

func reverse(s []byte, from int, to int) {
	for from < to {
		t := s[from]
		s[from] = s[to]
		s[to] = t
		from++
		to--
	}
}

func LeftShiftM_2(s []byte, m int) {
	m %= len(s)
	reverse(s, 0 , m -1)
	reverse(s, m, len(s) - 1)
	reverse(s, 0, len(s) - 1)
}

func main() {
	s := "ABCDEFG"
	s1 := []byte(s)

	LeftShiftM_1(s1, 3)
	fmt.Println(string(s1))

	fmt.Println("s: ", string(s))

	s2 := []byte(s)
	LeftShiftM_2(s2, 13)
	fmt.Println(string(s2))
}
