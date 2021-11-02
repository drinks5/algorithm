package painthouse

import (
	"fmt"

	"github.com/stretchr/testify/assert"

	"testing"
)

func Test_Main(t *testing.T) {
	type args struct {
		nums [][]int
	}
	tests := []struct {
		args args
		want int
	}{
		{args{[][]int{{17, 2, 17}, {16, 16, 5}, {14, 3, 19}}}, 10},
		{args{[][]int{{7, 6, 2}}}, 2},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := minCost(tt.args.nums); !assert.Equal(t, tt.want, got) {
				t.Errorf("main() = %v, want %v", got, tt.want)
			}
		})
	}
}
