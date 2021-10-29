package lengthOfLongestSubstring

import (
	"fmt"

	"github.com/stretchr/testify/assert"

	"testing"
)

func Test_Main(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		args args
		want int
	}{
		{args{"abcabcbb"}, 3},
		{args{"bbbbb"}, 1},
		{args{"pwwkew"}, 3},
		{args{""}, 0},
		{args{"abcabcbb"}, 3},
		{args{"aabaab!bb"}, 3},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := lengthOfLongestSubstring(tt.args.s); !assert.Equal(t, tt.want, got) {
				t.Errorf("main() = %v, want %v", got, tt.want)
			}
		})
	}
}
