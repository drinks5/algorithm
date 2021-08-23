package dividetwointegers

import "testing"

func TestDivide(t *testing.T) {
	table := []struct {
		in  [2]int
		out int
	}{
		{[2]int{1, 2}, 0},
		{[2]int{7, -3}, -2},
		{[2]int{15, 2}, 7},
		{[2]int{0, 1}, 0},
	}
	for _, tt := range table {
		t.Run("ok", func(t *testing.T) {
			s := Divide(tt.in[0], tt.in[1])
			if s != tt.out {
				t.Errorf("got %q, want %q", s, tt.out)
			}
		})
	}
}
