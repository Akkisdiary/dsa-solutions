"""
givne a base ttl and a list of queries as follows
ttl <int>
generate <token_id> <timestamp>
refresh <token_id> <timestamp>
count <timestamp>

for each generate query save the token with its expiry (timestamp + base ttl)
for each refresh query update the token's expiry
for each count queries count the number of unexpired tokens at that timestamp

return a list of integer representing the count of unexpired tokens for the corresponding queries
"""

from typing import List
from utils import TestRunner


class SolutionBrute:
    """time: O(queries * tokens) ; space: O(tokens + result)"""

    def solve(self, ttl: int, queries: List[int]) -> List[int]:
        result = []
        tokens = {}
        for q in queries:
            q = q.split(" ")
            if len(q) > 2:
                op, token, ts = q
                ts = int(ts)
                tokens[token] = ts + ttl

                # # case when token cannot be refreshed if already expired
                # if op == "generate":
                #     tokens[token] = ts + ttl
                # elif tokens[token] > ts:
                #     tokens[token] = ts + ttl
            else:
                op, ts = q
                ts = int(ts)
                result.append(self.countUnexpired(tokens, ts))
        return result

    def countUnexpired(self, tokens, timestamp):
        count = 0
        for t, ts in tokens.items():
            if ts > timestamp:
                count += 1
        return count


class SolutionBetter:
    """time: O(queries + tokens) ; space: O(tokens + tokens + result)"""

    def solve(self, ttl: int, queries: List[int]) -> List[int]:
        result, tokens, freq, i = [], [], {}, 0
        for q in queries:
            q = q.split(" ")
            if len(q) > 2:
                op, token, ts = q
                ts = int(ts)
                tokens.append((token, ts + ttl))
                freq[token] = freq.get(token, 0) + 1
            else:
                op, ts = q
                ts = int(ts)
                while i < len(tokens) and tokens[i][1] <= ts:
                    token = tokens[i][0]
                    f = freq.pop(token, 1) - 1
                    if f > 0:
                        freq[token] = f
                    i += 1
                result.append(len(freq))
        return result


cases = [
    {
        "input": {
            "ttl": 5,
            "queries": ["generate t1 1", "generate t2 2", "count 3"],
        },
        "expected": [2],
    },
    {
        "input": {
            "ttl": 5,
            "queries": [
                "generate t1 1",
                "generate t2 2",
                "count 3",
                "count 10",
            ],
        },
        "expected": [2, 0],
    },
    {
        "input": {
            "ttl": 5,
            "queries": [
                "generate t1 1",
                "generate t2 2",
                "count 3",
                "refresh t1 4",
                "count 7",
                "count 10",
            ],
        },
        "expected": [2, 1, 0],
    },
    {
        "input": {
            "ttl": 10,
            "queries": [
                "generate t1 2",
                "generate t2 5",
                "count 7",
                "refresh t1 10",
                "count 16",
                "count 20",
            ],
        },
        "expected": [2, 1, 0],
    },
    {
        "input": {
            "ttl": 10,
            "queries": [
                "generate t1 2",
                "generate t2 5",
                "count 7",
                "refresh t1 13",
                "count 16",
                "count 20",
            ],
        },
        "expected": [2, 1, 1],
    },
    {
        "input": {
            "ttl": 10,
            "queries": [
                "generate t1 1",
                "generate t2 2",
                "count 3",
                "generate t3 4",
                "count 5",
                "refresh t1 10",
                "refresh t1 11",
                "count 20",
                "count 30",
                "generate t4 31",
                "count 36",
            ],
        },
        "expected": [2, 3, 1, 0, 1],
    },
]

if __name__ == "__main__":
    TestRunner(SolutionBrute().solve).test(cases)
    TestRunner(SolutionBetter().solve).test(cases)
