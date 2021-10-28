package main

import (
	"fmt"

	"github.com/stretchr/testify/assert"

	"testing"
)

func Test_Main(t *testing.T) {
	type args struct {
		graph [][]int
	}
	tests := []struct {
		args args
		want [][]int
	}{
		{args{[][]int{{0, 0, 0}, {0, 1, 0}, {0, 0, 0}}}, [][]int{{0, 0, 0}, {0, 1, 0}, {0, 0, 0}}},
		{args{[][]int{{0, 0, 0}, {0, 1, 0}, {1, 1, 1}}}, [][]int{{0, 0, 0}, {0, 1, 0}, {1, 2, 1}}},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := updateMatrix(tt.args.graph); !assert.Equal(t, tt.want, got) {
				t.Errorf("main() = %v, want %v", got, tt.want)
			}
		})
	}
}
