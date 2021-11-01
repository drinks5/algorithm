package palindromepartitioning

import (
	"fmt"

	"github.com/stretchr/testify/assert"

	"testing"
)

func Test_Main(t *testing.T) {
	type args struct {
		target string
	}
	tests := []struct {
		args args
		want [][]string
	}{
		{args{"google"}, [][]string{{"g", "o", "o", "g", "l", "e"}, {"g", "oo", "g", "l", "e"}, {"goog", "l", "e"}}},
		{args{"aab"}, [][]string{{"a", "a", "b"}, {"aa", "b"}}},
		{args{"a"}, [][]string{{"a"}}},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := partition(tt.args.target); !assert.Equal(t, tt.want, got) {
				t.Errorf("main() = %v, want %v", got, tt.want)
			}
		})
	}
}
