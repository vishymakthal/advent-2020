package main

import (
	"bufio"
	"fmt"
	"os"
)

func howManyTrees(dx, dy int) int {

	f, _ := os.Open("./slope.txt")
	defer func() {
		f.Close()
	}()

	cnt := 0
	x := 0
	y := 0
	s := bufio.NewScanner(f)
	var ln string
	for s.Scan() {

		y++
		if y < dy {
			_ = s.Text()
		} else {
			y = 0
			ln = s.Text()
			if ln[x] == '#' {
				cnt++
			}
			x = (x + dx) % len(ln)
		}
	}

	return cnt
}

func main() {

	fmt.Printf("Ans part 1: %d\n", howManyTrees(3, 1))

	pairs := [][]int{
		[]int{1, 1},
		[]int{3, 1},
		[]int{5, 1},
		[]int{7, 1},
		[]int{1, 2},
	}

	res := 1
	for _, p := range pairs {
		res *= howManyTrees(p[0], p[1])
	}
	fmt.Printf("Ans part 2: %d\n", res)

}
