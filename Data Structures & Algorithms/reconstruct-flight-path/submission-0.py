from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)

        # 倒序排序
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        res = []

        def dfs(src):
            while graph[src]:
                dst = graph[src].pop()
                dfs(dst)

            res.append(src)

        dfs("JFK")

        return res[::-1]