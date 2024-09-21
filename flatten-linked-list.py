# Flatten A Linked List


# https://www.codingninjas.com/codestudio/problems/1112655?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None

    def __str__(self) -> str:
        return f"<Node {self.data}>"

    def __repr__(self) -> str:
        return f"<Node {self.data}>"

    def __del__(self):
        if self.next:
            del self.next


def flattenLinkedList(head):
    dummy = Node(None)
    dummy.next = head

    node = dummy.next
    pre = None

    while node and node.next:
        nxt = node.next
        child = node.child

        if pre and pre.data < nxt.data:
            pre.next = nxt
            node.next = pre
            pre = child
        else:
            if child and child.data <= nxt.data:
                child.next = nxt
                node.next = child
            if child and child.data > nxt.data:
                pre = child
            node = node.next

    return dummy.next


"""
3 4 6  -1
5 11 14 -1
22 25 -1
26 28 -1
39  -1
"""
l11 = Node(3)
l12 = Node(4)
l11.child = l12
l13 = Node(6)
l12.child = l13

l21 = Node(5)
l22 = Node(11)
l21.child = l22
l23 = Node(14)
l22.child = l23

l31 = Node(22)
l32 = Node(25)
l31.child = l32

l41 = Node(26)
l42 = Node(28)
l41.child = l42

l51 = Node(39)

l11.next = l21
l21.next = l31
l31.next = l41
l41.next = l51

flattenLinkedList(l11)
