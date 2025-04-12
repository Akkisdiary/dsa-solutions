# Cycle Detection In Undirected Graph

# https://www.codingninjas.com/codestudio/problems/1062670?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website


def getAdjList(n, m, edges):
    adj = [[] for _ in range(n + 1)]

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    return adj


def cycleDetection(edges, n, m):
    adj = getAdjList(n, m, edges)

    visited = [False] * (n + 1)
    ans = True

    for node in range(n + 1):
        if not visited[node]:
            queue = [node]
            while len(queue) > 0:
                curr = queue.pop(0)
                if curr != node and visited[curr]:
                    return "Yes"
                visited[curr] = True
                queue.extend(adj[curr])

    return "No"


print(cycleDetection([[1, 2], [2, 3]], 3, 2))
