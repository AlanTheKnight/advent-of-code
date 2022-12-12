package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	input, _ := os.ReadFile("input/day9.input.txt")
	fmt.Println("Part 1:", solve(string(input), 2))
	fmt.Println("Part 2:", solve(string(input), 10))
}

type Point struct {
	x int
	y int
}

func (p *Point) Add(other Point) {
	p.x += other.x
	p.y += other.y
}

func solve(input string, knots int) int {
	headMoves := map[byte]Point{'U': {0, 1}, 'D': {0, -1}, 'R': {1, 0}, 'L': {-1, 0}}

	rope := []*Point{}
	for len(rope) < knots {
		rope = append(rope, &Point{0, 0})
	}
	tailPositions := map[Point]int{{0, 0}: 1}

	moves := map[Point]Point{}
	moves[Point{0, -2}] = Point{0, -1}
	moves[Point{0, 2}] = Point{0, 1}
	moves[Point{-2, 0}] = Point{-1, 0}
	moves[Point{2, 0}] = Point{1, 0}
	moves[Point{2, 1}] = Point{1, 1}
	moves[Point{2, -1}] = Point{1, -1}
	moves[Point{-2, 1}] = Point{-1, 1}
	moves[Point{-2, -1}] = Point{-1, -1}
	moves[Point{1, 2}] = Point{1, 1}
	moves[Point{1, -2}] = Point{1, -1}
	moves[Point{-1, 2}] = Point{-1, 1}
	moves[Point{-1, -2}] = Point{-1, -1}
	moves[Point{-2, -2}] = Point{-1, -1}
	moves[Point{2, 2}] = Point{1, 1}
	moves[Point{-2, 2}] = Point{-1, 1}
	moves[Point{2, -2}] = Point{1, -1}

	for _, line := range strings.Split(input, "\n") {
		direction := strings.Fields(line)[0]
		dist, _ := strconv.Atoi(strings.Fields(line)[1])

		for i := 0; i < dist; i++ {
			// Head move
			rope[0].Add(headMoves[direction[0]])

			// Tail moves
			for k, v := range rope {
				if k != 0 {
					v.Add(moves[Point{rope[k-1].x - v.x, rope[k-1].y - v.y}])

					// Tracking rope's tail trace
					if k == len(rope)-1 {
						tailPositions[Point{v.x, v.y}] += 1
					}
				}
			}

		}
	}
	return len(tailPositions)
}
