# 3217. Delete Nodes From Linked List Present in Array
# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description


from utils import TestRunner, ListNode


class Solution:
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


cases = [
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
        "input": {"nums": [5], "head": ListNode.as_linked_list([1, 2, 3, 4])},
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

if __name__ == "__main__":
    TestRunner(Solution().modifiedList).test(
        cases, lambda x: list(sorted(x.as_list())) if x else x
    )
