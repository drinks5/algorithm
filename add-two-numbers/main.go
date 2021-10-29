package addtwonumbers

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	head := l1
	for {
		if l2 == nil && l1 == nil {
			break
		}
		if l1 == nil {
			l1 = &ListNode{Val: 0}
		}
		if l2 == nil {
			l2 = &ListNode{Val: 0}
		}
		l1.Val = l1.Val + l2.Val
		if l1.Val >= 10 {
			l1.Val = l1.Val - 10
			if l1.Next != nil {
				l1.Next.Val += 1
			} else {
				l1.Next = &ListNode{Val: 1}
			}
		}
		l1 = l1.Next
		l2 = l2.Next
	}
	return head
}
