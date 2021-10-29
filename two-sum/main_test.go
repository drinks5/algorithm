package main

import (
	"fmt"

	"github.com/stretchr/testify/assert"

	"testing"
)

func Test_Main(t *testing.T) {
	type args struct {
		nums   []int
		target int
	}
	tests := []struct {
		args args
		want []int
	}{
		{args{[]int{2, 7, 11, 15}, 9}, []int{0, 1}},
		{args{[]int{3, 2, 4}, 6}, []int{1, 2}},
		{args{[]int{3, 3}, 6}, []int{0, 1}},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := twoSum(tt.args.nums, tt.args.target); !assert.Equal(t, tt.want, got) {
				t.Errorf("main() = %v, want %v", got, tt.want)
			}
		})
	}
}
