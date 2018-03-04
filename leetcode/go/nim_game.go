package main

func canWinNim(n int) bool {
	/*
	1. The player who gets 4 stones will lose always. 4 is the death number.
	2. The player who gets 5,6,7 will let his/her competitor have 4 stones. So
	he will always win.
	3. The player who gets 8 stones will lose always. No matter how many stones
	he/she takes, his/her competitor will always have 5,6,7 stones.
	4. Likewise, we have the number N is a death number if n % 4 == 0.
	 */
	return n % 4 != 0
}

func main() {
}
