package singlenumberii

import "testing"

func TestAddBinary(t *testing.T) {
	table := []struct {
		in  []int
		out int
	}{
		{[]int{11, 10, 10, 10, 11, 11, 101}, 101},
	}
	for _, tt := range table {
		t.Run("ok", func(t *testing.T) {
			s := singleNumber(tt.in)
			if s != tt.out {
				t.Errorf("got %d, want %d", s, tt.out)
			}
		})
	}
}
