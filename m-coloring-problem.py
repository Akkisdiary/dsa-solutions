# M-Coloring Problem
# https://www.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1

from utils import TestRunner


class SolutionBrute:
    def graphColoring(self, v, edges, m):
        vColors = [-1] * v

        def isSafe(vertex, color):
            for left, right in edges:
                if vertex == left and vColors[right] == color:
                    return False
                if vertex == right and vColors[left] == color:
                    return False
            return True

        def solve(vertex):
            if vertex >= v:
                return True
            for color in range(m):
                if isSafe(vertex, color):
                    vColors[vertex] = color
                    if solve(vertex + 1):
                        return True
                    else:
                        vColors[vertex] = -1
            return False

        return solve(0)


cases = [
    {
        "input": {
            "v": 2,
            "edges": [(0, 1)],
            "m": 2,
        },
        "expected": True,
    },
    {
        "input": {
            "v": 2,
            "edges": [(0, 1)],
            "m": 1,
        },
        "expected": False,
    },
    {
        "input": {
            "v": 4,
            "edges": [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)],
            "m": 3,
        },
        "expected": True,
    },
    {
        "input": {
            "v": 3,
            "edges": [(0, 1), (1, 2), (0, 2)],
            "m": 2,
        },
        "expected": False,
    },
]

if __name__ == "__main__":
    TestRunner(SolutionBrute().graphColoring).test(cases)
