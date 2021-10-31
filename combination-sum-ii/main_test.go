package combinationSum

import (
	"fmt"

	"github.com/stretchr/testify/assert"

	"testing"
)

func Test_main(t *testing.T) {
	type args struct {
		arr []int
		k   int
	}
	tests := []struct {
		args args
		want [][]int
	}{
		{args{[]int{10, 1, 2, 7, 6, 1, 5}, 8}, [][]int{
			{1, 1, 6},
			{1, 2, 5},
			{1, 7},
			{2, 6},
		}},
		{args{[]int{2, 5, 2, 1, 2}, 5}, [][]int{
			{1, 2, 2},
			{5},
		}},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := combinationSum2(tt.args.arr, tt.args.k); !assert.Equal(t, tt.want, got) {
				t.Errorf("main() = %v, want %v", got, tt.want)
			}
		})
	}
}
