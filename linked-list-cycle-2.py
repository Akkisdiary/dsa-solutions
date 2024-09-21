# LinkedList Cycle II


# https://www.codingninjas.com/codestudio/problems/1112628?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None
        self.pos = []

    def __del__(self):
        if self.next:
            del self.next


def firstNode(head):
    memo = {}

    pos = 0
    node = head
    while node is not None:
        if node in memo:
            return memo[node]
        memo[node] = pos
        pos += 1
        node = node.next

    return -1


first = Node(1)

sec = Node(2)
first.next = sec

thir = Node(3)
sec.next = thir

four = Node(4)
thir.next = four

five = Node(5)
four.next = five

# five.next = four


print(firstNode(first))
