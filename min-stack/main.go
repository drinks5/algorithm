package main

type MinStack struct {
	min    int
	stack  []int
	length int
}

/** initialize your data structure here. */
func Constructor() MinStack {
	return MinStack{0, []int{}, 0}

}

func (this *MinStack) Push(x int) {
	if this.length == 0 {
		this.min = x
	} else if x <= this.min {
		this.stack = append(this.stack, this.min)
		this.min = x
		this.length += 1
	}
	this.stack = append(this.stack, x)
	this.length += 1
}

func (this *MinStack) Pop() {
	if this.length == 0 {
		return
	}
	if this.stack[this.length-1] == this.min {
		this.min = this.stack[this.length-2]
		this.stack = this.stack[:this.length-2]
		this.length -= 2
	} else {
		this.length -= 1
		this.stack = this.stack[:this.length-1]
	}
}

func (this *MinStack) Top() int {
	if this.length == 0 {
		return -(1 << 31)
	}
	return this.stack[this.length-1]

}

func (this *MinStack) Min() int {
	return this.min
}

func main() {
	stack := Constructor()
	stack.Push(2)
	stack.Push(0)
	stack.Push(3)
	stack.Push(0)
	stack.Pop()
	stack.Top()
	stack.Top()
	println(stack.min)
}
