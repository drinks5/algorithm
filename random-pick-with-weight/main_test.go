package main

import (
	"fmt"
	"testing"
)

func Test_singleNonDuplicate(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		args args
		want int
	}{
		{args{[]int{1, 1, 2, 3, 3, 4, 4, 8, 8}}, 2},
		{args{[]int{3, 3, 7, 7, 10, 11, 11}}, 10},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := singleNonDuplicate(tt.args.nums); got != tt.want {
				t.Errorf("singleNonDuplicate() = %v, want %v", got, tt.want)
			}
		})
	}
}
