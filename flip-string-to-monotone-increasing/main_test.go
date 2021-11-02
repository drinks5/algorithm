package flipstringtomonotoneincreasing

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
		{args: args{s: "00110"}, want: 1},
		{args: args{s: "010110"}, want: 2},
		{args: args{s: "00011000"}, want: 2},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := minFlipsMonoIncr(tt.args.s); !assert.Equal(t, tt.want, got) {
				t.Errorf("main() = %v, want %v", got, tt.want)
			}
		})
	}
}
