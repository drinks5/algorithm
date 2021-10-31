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
		{args{[]int{2, 3, 6, 7}, 7}, [][]int{{7}, {2, 2, 3}}},
		{args{[]int{2, 3, 5}, 8}, [][]int{{3, 5}, {2, 3, 3}, {2, 2, 2, 2}}},
		{args{[]int{2}, 1}, [][]int{}},
		{args{[]int{1}, 1}, [][]int{{1}}},
		{args{[]int{1}, 2}, [][]int{{1, 1}}},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := combinationSum(tt.args.arr, tt.args.k); !assert.Equal(t, tt.want, got) {
				t.Errorf("main() = %v, want %v", got, tt.want)
			}
		})
	}
}
