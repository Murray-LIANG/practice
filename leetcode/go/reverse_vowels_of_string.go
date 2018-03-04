package main

import "fmt"

func reverseVowels(s string) string {
	n := len(s)
	b := []byte(s)
	vowels := map[byte]bool{
		'a': true,
		'e': true,
		'i': true,
		'o': true,
		'u': true,
		'A': true,
		'E': true,
		'I': true,
		'O': true,
		'U': true,
	}
	for i, j := 0, n-1; i < j;{
		for ; i < j; i++ {
			if _, ok := vowels[b[i]]; ok {
				break
			}
		}
		for ; i < j; j-- {
			if _, ok := vowels[b[j]]; ok {
				break
			}
		}
		b[i], b[j] = b[j], b[i]
		i++
		j--
	}
	return string(b)

}

func main() {
	datas := []string{"Hello Ryan", "abc"}

	for i, data := range datas{
		fmt.Println(">>> Test Round #", i)
		fmt.Println("Input string: ", data)
		result := reverseVowels(data)
		fmt.Println("Result: ", result)
	}
}
