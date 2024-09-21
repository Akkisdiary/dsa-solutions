# 3217. Delete Nodes From Linked List Present in Array
# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description


from dsa.utils import TestRunner, ListNode


class SolutionBrute:
    def modifiedList(self, nums, head):
        parent = ListNode(next=head)
        memo = set(nums)

        prev = parent
        while prev.next is not None:
            node = prev.next
            if node.val not in memo:
                prev = node
            else:
                prev.next = node.next

        return parent.next


test_cases = [
    {
        "input": {
            "nums": [1, 2, 3],
            "head": ListNode.as_linked_list([1, 2, 3, 4, 5]),
        },
        "expected": ListNode.as_linked_list([4, 5]),
    },
    {
        "input": {
            "nums": [1],
            "head": ListNode.as_linked_list([1, 2, 1, 2, 1, 2]),
        },
        "expected": ListNode.as_linked_list([2, 2, 2]),
    },
    {
        "input": {
            "nums": [5],
            "head": ListNode.as_linked_list([1, 2, 3, 4]),
        },
        "expected": ListNode.as_linked_list([1, 2, 3, 4]),
    },
    {
        "input": {
            "nums": [5],
            "head": ListNode.as_linked_list([1, 2, 3, 4, 5]),
        },
        "expected": ListNode.as_linked_list([1, 2, 3, 4]),
    },
    {
        "input": {
            "nums": [1, 2, 3, 4, 5],
            "head": ListNode.as_linked_list([1, 2, 3, 4, 5]),
        },
        "expected": ListNode.as_linked_list([]),
    },
]
for case in test_cases:
    TestRunner(
        SolutionBrute().modifiedList,
    ).case(
        case
    ).test(
        lambda x: list(sorted(x.as_list())) if x else x
    )