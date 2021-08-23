package addbinary

import "testing"

func TestAddBinary(t *testing.T) {
	table := []struct {
		in  int
		out []int
	}{
		{2, []int{1, 0}},
		{2, []int{1, 2, 1, 0}},
	}
	for _, tt := range table {
		t.Run("ok", func(t *testing.T) {
			s := countBits(tt.in)
			println(&s)
		})
	}
}
