import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = {}

        for u, v, t in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, t))

        minHeap = [(0, k)]
        visited = set()

        res = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)

            res = max(res, time)

            for nei, weight in graph.get(node, []):
                if nei not in visited:
                    heapq.heappush(
                        minHeap,
                        (time + weight, nei)
                    )

        if len(visited) == n:
            return res

        return -1