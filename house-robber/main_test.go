package houserobber

import (
	"fmt"

	"github.com/stretchr/testify/assert"

	"testing"
)

func Test_Main(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		args args
		want int
	}{
		{args{[]int{1, 2, 3, 1}}, 4},
		{args{[]int{2, 7, 9, 3, 1}}, 12},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := rob(tt.args.nums); !assert.Equal(t, tt.want, got) {
				t.Errorf("main() = %v, want %v", got, tt.want)
			}
		})
	}
}
