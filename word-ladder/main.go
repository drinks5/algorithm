package main

import "math"

var (
	Dirs = [4][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
)

func updateMatrix(mat [][]int) [][]int {
	rows := len(mat)
	if rows == 0 {
		return [][]int{}
	}
	cols := len(mat[0])
	dists := make([][]int, rows)
	for i := range dists {
		dists[i] = make([]int, cols)
	}
	stack := [][2]int{}
	for i := range mat {
		for j := range mat[i] {
			if mat[i][j] == 0 {
				stack = append(stack, [2]int{i, j})
				dists[i][j] = 0
			} else {
				dists[i][j] = math.MaxInt64
			}
		}
	}
	var pos [2]int
	for {
		if len(stack) == 0 {
			break
		}
		pos, stack = stack[0], stack[1:]
		dist := dists[pos[0]][pos[1]] + 1
		for _, d := range Dirs {
			r := d[0] + pos[0]
			c := d[1] + pos[1]
			if 0 <= r && r < rows && 0 <= c && c < cols && dists[r][c] > dist {
				dists[r][c] = dist
				stack = append(stack, [2]int{r, c})
			}
		}
	}
	return dists
}
