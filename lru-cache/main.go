package lrucache

type Node struct {
	key  int
	val  int
	pre  *Node
	next *Node
}

func (n *Node) delete() {
	n.pre.next = n.next
	n.next.pre = n.pre
}

type LRUCache struct {
	capacity  int
	nodeByKey map[int]*Node
	head      *Node
	tail      *Node
}

func Constructor(capacity int) LRUCache {
	head := Node{key: -1, val: -1}
	tail := Node{key: -1, val: -1}
	tail.pre = &head
	head.next = &tail
	nodeByKey := make(map[int]*Node)
	return LRUCache{capacity: capacity, nodeByKey: nodeByKey, head: &head, tail: &tail}
}

func (this *LRUCache) Get(key int) int {
	node, ok := this.nodeByKey[key]
	if !ok {
		return -1
	}
	this.move2Tail(node, node.val)
	return node.val
}

func (this *LRUCache) Put(key int, value int) {
	if node, ok := this.nodeByKey[key]; ok {
		this.move2Tail(node, value)
		return
	}
	if len(this.nodeByKey) == this.capacity {
		delete(this.nodeByKey, this.head.next.key)
		this.head.next.delete()
	}
	node := &Node{key: key, val: value}
	this.insert2Tail(node)
	this.nodeByKey[key] = node
}

func (this *LRUCache) move2Tail(node *Node, val int) {
	node.delete()
	node.val = val
	this.insert2Tail(node)
}

func (this *LRUCache) insert2Tail(node *Node) {
	this.tail.pre.next = node
	node.pre = this.tail.pre
	node.next = this.tail
	this.tail.pre = node
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
