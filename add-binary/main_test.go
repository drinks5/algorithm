package addbinary

import "testing"

func TestAddBinary(t *testing.T) {
	table := []struct {
		in  [2]string
		out string
	}{
		{[2]string{"11", "10"}, "101"},
	}
	for _, tt := range table {
		t.Run("ok", func(t *testing.T) {
			s := addBinary(tt.in[0], tt.in[1])
			if s != tt.out {
				t.Errorf("got %q, want %q", s, tt.out)
			}
		})
	}
}
