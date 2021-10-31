package combinations

import (
	"fmt"

	"github.com/stretchr/testify/assert"

	"testing"
)

func Test_Main(t *testing.T) {
	type args struct {
		n int
		k int
	}
	tests := []struct {
		args args
		want [][]int
	}{
		{args{4, 2}, [][]int{
			{2, 4},
			{3, 4},
			{2, 3},
			{1, 2},
			{1, 3},
			{1, 4},
		}},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := combine(tt.args.n, tt.args.k); !assert.Equal(t, tt.want, got) {
				t.Errorf("main() = %v, want %v", got, tt.want)
			}
		})
	}
}
