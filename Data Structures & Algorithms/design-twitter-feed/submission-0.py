import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.time = 0

        # userId -> [(time, tweetId)]
        self.tweetMap = defaultdict(list)

        # followerId -> {followeeId}
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # 自己的 tweet 也必须出现在 feed
        self.followMap[userId].add(userId)

        # 把每个关注用户最新的一条 tweet 放入 heap
        for followeeId in self.followMap[userId]:

            if followeeId in self.tweetMap and self.tweetMap[followeeId]:

                index = len(self.tweetMap[followeeId]) - 1

                time, tweetId = self.tweetMap[followeeId][index]

                heapq.heappush(
                    minHeap,
                    (-time, tweetId, followeeId, index - 1)
                )

        # 最多取 10 条
        while minHeap and len(res) < 10:

            negTime, tweetId, followeeId, index = heapq.heappop(minHeap)

            res.append(tweetId)

            # 如果这个用户还有更早的 tweet
            if index >= 0:

                time, nextTweetId = self.tweetMap[followeeId][index]

                heapq.heappush(
                    minHeap,
                    (-time, nextTweetId, followeeId, index - 1)
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)