package lrucache

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestLrcCache(t *testing.T) {
	c := Constructor(2)
	c.Put(1, 1)
	c.Put(2, 2)
	assert.Equal(t, 1, c.Get(1))
	c.Put(3, 3)
	assert.Equal(t, -1, c.Get(2))
	c.Put(4, 4)
	assert.Equal(t, -1, c.Get(1))
	assert.Equal(t, 3, c.Get(3))
	assert.Equal(t, 4, c.Get(4))
}
