package main

import (
	"fmt"

	"github.com/stretchr/testify/assert"

	"testing"
)

func Test_findKthLargest(t *testing.T) {
	type args struct {
		arr []int
		k   int
	}
	tests := []struct {
		args args
		want int
	}{
		{args{[]int{3, 2, 1, 5, 6, 4}, 2}, 5},
		{args{[]int{3, 2, 3, 1, 2, 4, 5, 5, 6}, 4}, 4},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := findKthLargest(tt.args.arr, tt.args.k); !assert.Equal(t, tt.want, got) {
				t.Errorf("singleNonDuplicate() = %v, want %v", got, tt.want)
			}
		})
	}
}
