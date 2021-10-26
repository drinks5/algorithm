package main

import (
	"fmt"
	"testing"
)

func Test_sqrt(t *testing.T) {
	tests := []struct {
		args int
		want int
	}{
		{4, 2},
		{8, 2},
		{16, 4},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := mySqrt(tt.args); got != tt.want {
				t.Errorf("sqrt() = %v, want %v", got, tt.want)
			}
		})
	}
}
