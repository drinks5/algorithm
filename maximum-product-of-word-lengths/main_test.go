package maximumproductofwordlengths

import (
	"testing"
)

func Test_maxProduct(t *testing.T) {
	type args struct {
		words []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"1", args{[]string{"ab", "cd"}}, 4},
		{"2", args{[]string{"a", "ab", "abc", "d", "cd", "bcd", "abcd"}}, 4},
		{"3", args{[]string{"a", "aa", "aaa", "aaaa"}}, 0},
		{"4", args{[]string{}}, 0},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxProduct(tt.args.words); got != tt.want {
				t.Errorf("maxProduct() = %v, want %v", got, tt.want)
			}
		})
	}
}
