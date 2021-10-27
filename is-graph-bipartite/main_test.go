package main

import (
	"fmt"

	"github.com/stretchr/testify/assert"

	"testing"
)

func Test_(t *testing.T) {
	type args struct {
		graph [][]int
	}
	tests := []struct {
		args args
		want bool
	}{
		{args{[][]int{{1, 3}, {0, 2}, {1, 3}, {0, 2}}}, true},
		{args{[][]int{{1, 2, 3}, {0, 2}, {0, 1, 3}, {0, 2}}}, false},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := isBipartite(tt.args.graph); !assert.Equal(t, tt.want, got) {
				t.Errorf("main() = %v, want %v", got, tt.want)
			}
		})
	}
}
