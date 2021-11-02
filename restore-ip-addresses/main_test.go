package restoreIpAddresses

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
		want []string
	}{
		{args{"25525511135"}, []string{"255.255.11.135", "255.255.111.35"}},
		{args{"0000"}, []string{"0.0.0.0"}},
		{args{"1111"}, []string{"1.1.1.1"}},
		{args{"010010"}, []string{"0.10.0.10", "0.100.1.0"}},
		{args{"10203040"}, []string{"10.20.30.40", "10.203.0.40", "102.0.30.40"}},
	}
	for i, tt := range tests {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := restoreIpAddresses(tt.args.target); !assert.Equal(t, tt.want, got) {
				t.Errorf("main() = %v, want %v", got, tt.want)
			}
		})
	}
}
