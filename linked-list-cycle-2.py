# LinkedList Cycle II
# https://www.codingninjas.com/codestudio/problems/1112628
# https://leetcode.com/problems/linked-list-cycle-ii/description/

from utils import ListNode


class SolutionBrute:
    def detectCycle(self, head):
        memo = set()
        while head:
            if head in memo:
                return head
            memo.add(head)
            head = head.next


class SolutionBetter:
    def detectCycle(self, head):
        d = ListNode(next=head)
        slow = d.next
        fast = d.next
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        slow = d.next
        while slow and fast and fast.next:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next


head1 = ListNode.as_linked_list([3, 2, 0, -4], pos=1)
head2 = ListNode.as_linked_list([1, 2], pos=0)
head3 = ListNode.as_linked_list([1], pos=-1)
head4 = ListNode.as_linked_list(
    [
        7032, 15013, 6890, 8877, 11344, 320, 13037, 9414, 6817, 1566,
        14907, -2756, 9931, -4488, 11602, 4887, 1239, 6231
    ],
    pos=-1,
)

print(SolutionBetter().detectCycle(head1))
print(SolutionBetter().detectCycle(head2))
print(SolutionBetter().detectCycle(head3))
print(SolutionBetter().detectCycle(head4))
