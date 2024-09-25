# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/


from utils import TestRunner, ListNode


class Solution:
    def reverseList(self, head):
        return self.solve(head, None)

    def solve(self, head, prev):
        if head is None:
            return prev
        nxt = head.next
        head.next = prev
        return self.solve(nxt, head)


test_cases = [
    {
        "input": {
            "head": ListNode.as_linked_list([1, 2, 3, 4, 5]),
        },
        "expected": ListNode.as_linked_list([5, 4, 3, 2, 1]),
    },
    {
        "input": {
            "head": ListNode.as_linked_list([1, 2]),
        },
        "expected": ListNode.as_linked_list([2, 1]),
    },
    {
        "input": {
            "head": ListNode.as_linked_list([]),
        },
        "expected": ListNode.as_linked_list([]),
    },
    {
        "input": {
            "head": ListNode.as_linked_list([1]),
        },
        "expected": ListNode.as_linked_list([1]),
    },
]
for case in test_cases:
    TestRunner(Solution().reverseList).case(case).test(
        lambda x: x.as_list() if x else []
    )
