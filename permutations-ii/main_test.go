package permuteUnique

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
		{args{[]int{1, 1, 2}}, [][]int{{1, 1, 2}, {1, 2, 1}, {2, 1, 1}}},
		{args{[]int{1, 2, 3}}, [][]int{
			{1, 2, 3},
			{1, 3, 2},
			{2, 1, 3},
			{2, 3, 1},
			{3, 1, 2},
			{3, 2, 1},
		}},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := permuteUnique(tt.args.arr); !assert.Equal(t, tt.want, got) {
				t.Errorf("main() = %v, want %v", got, tt.want)
			}
		})
	}
}
