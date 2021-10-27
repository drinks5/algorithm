package main

import (
	"fmt"

	"github.com/stretchr/testify/assert"

	"testing"
)

func Test_relativeSortArray(t *testing.T) {
	type args struct {
		arr1 []int
		arr2 []int
	}
	tests := []struct {
		args args
		want []int
	}{
		{args{[]int{2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19}, []int{2, 1, 4, 3, 9, 6}}, []int{2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19}},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := relativeSortArray(tt.args.arr1, tt.args.arr2); !assert.Equal(t, tt.want, got) {
				t.Errorf("singleNonDuplicate() = %v, want %v", got, tt.want)
			}
		})
	}
}
