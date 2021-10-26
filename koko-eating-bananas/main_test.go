package main

import (
	"fmt"
	"testing"
)

func Test_singleNonDuplicate(t *testing.T) {
	type args struct {
		nums []int
		h    int
	}
	tests := []struct {
		args args
		want int
	}{
		{args{[]int{3, 6, 7, 11}, 8}, 4},
		{args{[]int{30, 11, 23, 4, 20}, 5}, 30},
		{args{[]int{30, 11, 23, 4, 20}, 6}, 23},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := minEatingSpeed(tt.args.nums, tt.args.h); got != tt.want {
				t.Errorf("singleNonDuplicate() = %v, want %v", got, tt.want)
			}
		})
	}
}
