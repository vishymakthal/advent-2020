package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var (
	ln string
)

func getID(ec string) int {

	var l = 0
	var r = 127
	for i := 0; i < 7; i++ {

		mid := l + (r-l)/2
		if ec[i] == 'F' {
			r = mid
		} else {
			l = mid
		}
	}
	row := r

	l = 0
	r = 7
	for i := 7; i < len(ec); i++ {
		mid := l + (r-l)/2
		if ec[i] == 'L' {
			r = mid
		} else {
			l = mid
		}
	}
	col := r

	return row*8 + col
}

func main() {

	// file open & close
	f, _ := os.Open("./in.txt")
	defer func() {
		f.Close()
	}()

	// problem specific vars
	maxVal := 0
	minVal := math.MaxInt64
	sum := 0.0

	// going through the lines
	s := bufio.NewScanner(f)
	for s.Scan() {
		ln = s.Text()

		id := float64(getId(ln))
		maxVal = int(math.Max(float64(maxVal), id))
		minVal = int(math.Min(float64(minVal), id))

		sum += id
	}

	fmt.Printf("Ans part 1: %d\n", maxVal)

	t := 0
	for n := minVal; n <= maxVal; n++ {
		t += n
	}

	fmt.Printf("Ans part 2: %d\n", t-int(sum))
}
