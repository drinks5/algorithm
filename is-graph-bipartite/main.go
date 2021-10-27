package main

func isBipartite(graph [][]int) bool {
	length := len(graph)
	colors := make([]int, length)
	for i := range colors {
		colors[i] = -1
	}
	for i := 0; i < length; i++ {
		if colors[i] == -1 {
			if !setColorBFS(graph, colors, i, 0) {
				return false
			}
		}
	}

	return true
}

func setColor(graph [][]int, colors []int, i, color int) bool {
	if colors[i] >= 0 {
		return colors[i] == color
	}
	colors[i] = color
	for _, n := range graph[i] {
		if !setColor(graph, colors, n, 1-color) {
			return false
		}
	}
	return true
}

func setColorBFS(graph [][]int, colors []int, i, color int) bool {
	var v int
	stack := []int{i}
	colors[i] = color
	for {
		if len(stack) == 0 {
			break
		}
		v, stack = stack[0], stack[1:]
		for _, n := range graph[v] {
			if colors[n] >= 0 {
				if colors[n] == colors[v] {
					return false
				}
			} else {
				stack = append(stack, n)
				colors[n] = 1 - colors[v]
			}

		}
	}
	return true
}
