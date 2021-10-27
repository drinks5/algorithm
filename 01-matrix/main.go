package main

var (
	Dirs = [4][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
)

func maxAreaOfIsland(grid [][]int) int {
	area := 0
	rows := len(grid)
	if rows == 0 {
		return 0
	}
	cols := len(grid[0])
	visited := make([][]bool, rows)
	for v := range visited {
		visited[v] = make([]bool, cols)
	}
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if (grid[i][j] == 1) && !visited[i][j] {
				if a := getAreaDFS(grid, visited, i, j, rows, cols); a > area {
					area = a
				}
			}
		}
	}
	return area
}

func getArea(grid [][]int, visited [][]bool, i, j, rows, cols int) int {
	var pos [2]int
	stack := [][2]int{{i, j}}
	visited[i][j] = true
	area := 0
	for {
		if len(stack) == 0 {
			break
		}
		area++
		pos, stack = stack[0], stack[1:]
		for _, d := range Dirs {
			r := pos[0] + d[0]
			c := pos[1] + d[1]
			if 0 <= r && r < rows && 0 <= c &&
				c < cols && grid[r][c] == 1 &&
				!visited[r][c] {
				stack = append(stack, [2]int{r, c})
				visited[r][c] = true
			}
		}
	}
	return area
}

func getAreaDFS(grid [][]int, visited [][]bool, i, j, rows, cols int) int {
	var area int
	if 0 <= i && i < rows && 0 <= j &&
		j < cols && grid[i][j] == 1 &&
		!visited[i][j] {
		area = 1
	} else {
		return 0
	}
	visited[i][j] = true
	for _, d := range Dirs {
		area += getAreaDFS(grid, visited, i+d[0], j+d[1], rows, cols)
	}
	return area
}
