import heapq
from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        # Memory O(n*k+n*t) where n=#users, k=#followers t=#tweets
        self.count = 0  # proxy for timestamp
        self.user_tweets = defaultdict(list)  # user: maxheap [count, tweet ids]
        self.follower_map = defaultdict(set)  # user: {user ids}

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Time O(1)
        self.user_tweets[userId].append([self.count, tweetId])
        self.count -= 1  # key in maxheap

    def getNewsFeed(self, userId: int) -> List[int]:
        # Time O(10 log k) where k=#followers
        res = []
        heap = []
        self.follower_map[userId].add(userId)
        for followeeId in self.follower_map[userId]:
            if self.user_tweets[followeeId]:
                index = len(self.user_tweets[followeeId]) - 1
                count, tweet_id = self.user_tweets[followeeId][index]
                heap.append([count, tweet_id, followeeId, index - 1])
        heapq.heapify(heap)
        while heap and len(res) < 10:
            count, tweet_id, followeeId, i = heapq.heappop(heap)
            res.append(tweet_id)
            if i >= 0:
                next_count, next_tweet_id = self.user_tweets[followeeId][i]
                heapq.heappush(heap, [next_count, next_tweet_id, followeeId, i - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # Time O(1)
        self.follower_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Time O(1)
        self.follower_map[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
