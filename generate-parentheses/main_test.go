package generateParenthesis

import (
	"fmt"

	"github.com/stretchr/testify/assert"

	"testing"
)

func Test_main(t *testing.T) {
	type args struct {
		n int
	}
	tests := []struct {
		args args
		want []string
	}{
		{args{3}, []string{"((()))", "(()())", "(())()", "()(())", "()()()"}},
		{args{1}, []string{"()"}},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := generateParenthesis(tt.args.n); !assert.Equal(t, tt.want, got) {
				t.Errorf("main() = %v, want %v", got, tt.want)
			}
		})
	}
}
