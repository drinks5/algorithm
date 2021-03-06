package permutations

import (
	"fmt"

	"github.com/stretchr/testify/assert"

	"testing"
)

func Test_main(t *testing.T) {
	type args struct {
		arr []int
	}
	tests := []struct {
		args args
		want [][]int
	}{
		{args{[]int{1, 2, 3}}, [][]int{
			{1, 2, 3},
			{1, 3, 2},
			{2, 1, 3},
			{2, 3, 1},
			{3, 2, 1},
			{3, 1, 2},
		}},
		{args{[]int{0, 1}}, [][]int{{0, 1}, {1, 0}}},
		{args{[]int{1}}, [][]int{{1}}},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := permute(tt.args.arr); !assert.Equal(t, tt.want, got) {
				t.Errorf("main() = %v, want %v", got, tt.want)
			}
		})
	}
}
