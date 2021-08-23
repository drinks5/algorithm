package addbinary

import "testing"

func TestAddBinary(t *testing.T) {
	table := []struct {
		in  [][]int
		out [][]int
	}{
		{[][]int{{1, 3}, {2, 6}, {8, 10}, {15, 18}}, [][]int{{1, 6}, {8, 10}, 15, 18}},
	}
	for _, tt := range table {
		t.Run("ok", func(t *testing.T) {
			s := merge(tt.in)
		})
	}
}
