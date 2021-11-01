package singlenumberii

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_main(t *testing.T) {
	type args struct {
		arr []int
	}
	tests := []struct {
		args args
		want int
	}{
		{args{[]int{2, 2, 3, 2}}, 3},
		{args{[]int{0, 1, 0, 1, 0, 1, 100}}, 100},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := singleNumber(tt.args.arr); !assert.Equal(t, tt.want, got) {
				t.Errorf("main() = %v, want %v", got, tt.want)
			}
		})
	}
}
