class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class SolutionRecursion:
    def level_order(self, root):
        ans = []

        def solve(roots):
            if not roots:
                return
            parents = []
            children = []
            for r in roots:
                if r:
                    parents.append(r.data)
                    children.append(r.left)
                    children.append(r.right)
            if parents:
                ans.append(parents)
            if children:
                solve(children)

        solve([root])
        return ans


class SolutionQueue:
    def level_order(self, root):
        ans = []
        queue = [root]
        while len(queue) > 0:
            children = []
            ans.append([])
            while len(queue) > 0:
                node = queue.pop(0)
                ans[-1].append(node.data)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            queue = children
        return ans


if __name__ == "__main__":
    #       5
    #      / \
    #    12   13
    #    /  \    \
    #   7    14    2
    #  /  \   /  \  / \
    # 17  23 27  3  8  11

    root = Node(5)
    root.left = Node(12)
    root.right = Node(13)

    root.left.left = Node(7)
    root.left.right = Node(14)

    root.right.right = Node(2)

    root.left.left.left = Node(17)
    root.left.left.right = Node(23)

    root.left.right.left = Node(27)
    root.left.right.right = Node(3)

    root.right.right.left = Node(8)
    root.right.right.right = Node(11)

    res = SolutionQueue().level_order(root)
    print(res)
