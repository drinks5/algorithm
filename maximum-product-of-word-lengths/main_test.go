package maximumproductofwordlengths

import "testing"

func TestAddBinary(t *testing.T) {
	table := []struct {
		in  []string
		out int
	}{
		{[]string{"11", "10"}, 101},
	}
	for _, tt := range table {
		t.Run("ok", func(t *testing.T) {
			s := maxProduct(tt.in)
			if s != tt.out {
				t.Errorf("got %q, want %q", s, tt.out)
			}
		})
	}
}
