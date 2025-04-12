# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/


from utils import TestRunner, ListNode


class SolutionRecursive:
    def reverseList(self, head):
        return self.solve(head, None)

    def solve(self, head, prev):
        if head is None:
            return prev
        nxt = head.next
        head.next = prev
        return self.solve(nxt, head)


class SolutionLoop:
    def reverseList(self, head):
        if not head:
            return head
        prev = None
        while head.next:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        head.next = prev
        return head


cases = [
    {
        "input": {"head": ListNode.as_linked_list([1, 2, 3, 4, 5])},
        "expected": ListNode.as_linked_list([5, 4, 3, 2, 1]),
    },
    {
        "input": {"head": ListNode.as_linked_list([1, 2])},
        "expected": ListNode.as_linked_list([2, 1]),
    },
    {
        "input": {"head": ListNode.as_linked_list([])},
        "expected": ListNode.as_linked_list([]),
    },
    {
        "input": {"head": ListNode.as_linked_list([1])},
        "expected": ListNode.as_linked_list([1]),
    },
    {
        "input": {"head": ListNode.as_linked_list([3, 2, 1, 3, 2, 3])},
        "expected": ListNode.as_linked_list([3, 2, 3, 1, 2, 3]),
    },
]

if __name__ == "__main__":
    TestRunner(SolutionLoop().reverseList).test(
        cases, lambda x: x.as_list() if x else []
    )
