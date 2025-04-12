# Flatten A Linked List
# https://www.codingninjas.com/codestudio/problems/1112655
# https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None

    def __str__(self) -> str:
        return f"<Node {self.data}>"

    def __repr__(self) -> str:
        return f"<Node {self.data}>"

    def __del__(self):
        if self.next:
            del self.next


class Solution:
    def flatten(self, root):
        d = Node(-1)
        d.bottom = root
        head = d.bottom
        if not head:
            return head
        nxt = self.flatten(head.next)
        return self.merge(head, nxt)

    def merge(self, h1, h2):
        d = Node(-1)
        head = d
        while h1 and h2:
            if h1.data < h2.data:
                head.bottom = h1
                h1 = h1.bottom
            else:
                head.bottom = h2
                h2 = h2.bottom
            head = head.bottom
        if h1:
            head.bottom = h1
        if h2:
            head.bottom = h2
        return d.bottom


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

# print(flattenLinkedList(l11))


"""
10 19 17 15
1 3 5 5 6 7 8 9 9 10 1 1 1 1 3 4 4 5 5 6 6 7 7 8 8 8 9 9 10 1 1 1 2 5 6 8 8 8 8 8 8 9 9 9 10 10 1 2 2 3 5 5 5 7 7 8 8 9 9 9 10
"""


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.bottom

    print()


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        head = None
        arr = []

        arr = [int(x) for x in input().strip().split()]
        N = len(arr)
        temp = None
        tempB = None
        pre = None
        preB = None

        flag = 1
        flag1 = 1
        listo = [int(x) for x in input().strip().split()]
        it = 0
        for i in range(N):
            m = arr[i]
            m -= 1
            a1 = listo[it]
            it += 1
            temp = Node(a1)
            if flag == 1:
                head = temp
                pre = temp
                flag = 0
                flag1 = 1
            else:
                pre.next = temp
                pre = temp
                flag1 = 1

            for j in range(m):
                a = listo[it]
                it += 1
                tempB = Node(a)
                if flag1 == 1:
                    temp.bottom = tempB
                    preB = tempB
                    flag1 = 0
                else:
                    preB.bottom = tempB
                    preB = tempB
        ob = Solution()
        root = ob.flatten(head)
        printList(root)

        t -= 1
